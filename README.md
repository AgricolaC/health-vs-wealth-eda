# 🌍 Health vs Life Expectancy EDA

This project investigates the global relationship between health expenditure and life expectancy using real-world datasets from the World Bank. It explores patterns of inequality, uncovers hidden inefficiencies, and builds modular, reusable visualizations and metrics.

## 📌 Goals

- Explore how different types of health spending relate to life expectancy.
- Visualize inequality in global health outcomes and investments.
- Highlight countries that overperform or underperform for their level of spending.
- Create a visually compelling and reproducible EDA pipeline.

## 📊 Highlights

- 📈 Histograms, scatter plots, and regression analysis across multiple metrics:
  - Per capita spending
  - PPP-adjusted spending
  - Total spending
  - % of GDP
- 📉 Inequality measures: Gini coefficients and Lorenz curves
- ✅ Efficiency frontier analysis using log-linear regression residuals
- 🌎 Country-level case studies and regional performance insights
- 🔁 Modular Plotly dashboard with year-by-year animation

## 📂 Structure

- `eda_health_vs_life.ipynb`: Full Jupyter notebook analysis
- `data/`: Cleaned and processed health + life expectancy data
- `images/`: Visual assets (e.g., plots)
- `interactive/`: Plotly HTML dashboard
- `walkthrough.md`: Markdown storytelling version for web publication

## 🛠 Technologies

- Python (Pandas, NumPy, Scikit-learn)
- Seaborn, Matplotlib, Plotly
- Jupyter Notebook
- Astro + TailwindCSS (for deployment)

## 📎 Data Sources

- World Bank: Health Nutrition and Population Statistics
- World Bank: Life Expectancy at Birth

---

© 2025 Berk Çalışır | README file generated with LLM, used after minor editing.
