import pandas as pd
import os

RAW_DATA_DIR = 'data/raw'
PROCESSED_DATA_DIR = 'data/processed'

def load_first():
    "Load the health data from the raw directory without any preprocessing to analyse the columns and data types."
    # Load both
    health_df = pd.read_csv("data/raw/health-nutrition-and-population-statisticse.csv", skiprows=4)
    life_df = pd.read_csv("data/raw/life-expectancy.csv", skiprows=4)

    # Explore unique indicators in the health dataset
    print("Health Indicators:\n", health_df["Indicator Name"].unique())
    print("Health Indicator Codes:\n", health_df["Indicator Code"].unique())

    # Check if the life expectancy file has multiple indicators
    print("Life Expectancy Indicator Name:", life_df["Indicator Name"].unique())
    print("Life Expectancy Indicator Code:", life_df["Indicator Code"].unique())

load_first()

#def load_health_data():
    #path = os.path.join(RAW_DATA_DIR, 'health-nutrition-and-population-statistics.csv')