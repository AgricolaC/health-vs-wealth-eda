import pandas as pd
import os

RAW_DATA_DIR = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'

def load_first():
    "Load the health data from the raw directory without any preprocessing to analyse the columns and data types."
    health_df = pd.read_csv("data/raw/health-nutrition-and-population-statistics.csv")
    life_df = pd.read_csv("data/raw/life-expectancy/life-expectancy.csv")

    print("Health Indicators:\n", health_df["Indicator Name"].unique())
    print("Health Indicator Codes:\n", health_df["Indicator Code"].unique())

# load_first()

# Target indicators
INDICATORS_TO_KEEP = {
    "SH.XPD.PCAP": "health_exp_per_capita", # Health expenditure per capita (current US$)
    "SH.XPD.PCAP.PP.KD": "health_exp_ppp_per_capita", # Health expenditure per capita, PPP
    "SH.XPD.TOTL.ZS": "health_exp_percent", # Health expenditure, total (% of GDP)
    "SH.XPD.TOTL.CD": "health_exp_total", # Health expenditure, total (current US$)
}

def load_and_clean_health_data():
    path = os.path.join(RAW_DATA_DIR, "health-nutrition-and-population-statistics.csv")
    print("\n" + "="*50)
    print(f"Loading health expenditure data from: {path}")
    df = pd.read_csv(path)
    print("Health Expenditure Data Raw shape:", df.shape)

    df = df[df["Indicator Code"].isin(INDICATORS_TO_KEEP.keys())]
    print("After filtering indicators:", df["Indicator Code"].unique())
    print("Filtered shape:", df.shape)

    
    year_cols = [col for col in df.columns if col.isdigit() and 1950 <= int(col) <= 2025]
    id_cols = ["Country Name", "Country Code", "Indicator Code"]

    # Melt from wide to long
    df_long = df.melt(
        id_vars=id_cols,
        value_vars=year_cols,
        var_name="Year",
        value_name="Value"
    )
    
    df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")
    before_drop = df_long.shape[0]
    df_long.dropna(subset=["Value", "Year"], inplace=True)
    print(f"Dropped {before_drop - df_long.shape[0]} rows with missing values")


    df_long["Indicator"] = df_long["Indicator Code"].map(INDICATORS_TO_KEEP)

    df_pivot = df_long.pivot_table(
        index=["Country Name", "Country Code", "Year"],
        columns="Indicator",
        values="Value"
    ).reset_index()
    
    print("Cleaned health data shape:", df_pivot.shape)
    print("Health data years:", df_pivot["Year"].min(), "-", df_pivot["Year"].max())

    return df_pivot

def load_and_clean_life_expectancy():
    path = os.path.join(RAW_DATA_DIR, "life-expectancy/life-expectancy.csv")
    print("\n" + "="*50)
    print(f"Loading life expectancy data from: {path}")
    df = pd.read_csv(path)
    print("Life Expectancy Data Raw shape:", df.shape)

    df = df.rename(columns={
        "Entity": "Country Name",
        "Code": "Country Code",
        "Period life expectancy at birth - Sex: total - Age: 0": "Life Expectancy"
    })
    
    if not all(col in df.columns for col in ["Year", "Country Name", "Country Code", "Life Expectancy"]):
        raise ValueError("Expected columns not found in life expectancy file")

    # Ensure year is numeric and within the correct range
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df[df["Year"].between(1950, 2025)]

    before_drop = df.shape[0]
    df = df.dropna(subset=["Life Expectancy", "Year", "Country Code"])
    print(f"Dropped {before_drop - df.shape[0]} rows with missing values")
    
    print("Cleaned life data shape:", df.shape)
    print("Life data years:", df['Year'].min(), "-", df['Year'].max())
    print("Countries:", df['Country Name'].nunique())
    print("\n")

    return df


def merge_and_save():
    df_health = load_and_clean_health_data()
    df_life = load_and_clean_life_expectancy()

    df_life = df_life.drop(columns=["Country Name"])
    df = pd.merge(df_health, df_life, on=["Country Code", "Year"], how="inner")
    print("\n" + "="*50)
    print("Merged shape:", df.shape)

    if df.empty:
        raise ValueError("Merged dataset is empty. Check for non-overlapping countries/years.")
    
    # Optional: Keep one Country Name column for readability
    df = df.drop_duplicates(subset=["Country Code", "Year"])
    df = df.sort_values(["Country Code", "Year"])

    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    out_path = os.path.join(PROCESSED_DATA_DIR, "health_vs_life.csv")
    df.to_csv(out_path, index=False)
    print(f"✅ Saved cleaned dataset to {out_path}")

if __name__ == "__main__":
    merge_and_save()
