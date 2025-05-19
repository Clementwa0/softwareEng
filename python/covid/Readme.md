# 📊 COVID-19 Data Visualization and Analysis

A Python-based data analysis project exploring the spread and impact of COVID-19 across Kenya, the United States, and India using OWID (Our World in Data) datasets. The project includes visualizations for total cases, deaths, vaccinations, and death rates over time, as well as an optional global choropleth map.

---

## 🎯 Objectives

- Clean and prepare COVID-19 data for analysis
- Perform Exploratory Data Analysis (EDA) on selected countries
- Visualize trends in total cases, deaths, new cases, death rates, and vaccinations
- Create a global map to visualize the distribution of total cases
- Derive insights from the trends and patterns observed

---

## 🧰 Tools and Libraries Used

- **Python** (3.7+)
- **Pandas** – data manipulation
- **Matplotlib** – basic plotting
- **Seaborn** – enhanced visual aesthetics
- **Plotly Express** – interactive choropleth map

---

## 🚀 How to Run the Project

1. **Clone the repository** or download the files.
2. **Install required packages**:
   ```bash
   pip install pandas matplotlib seaborn plotly
   ```
3. **Download the dataset**:
   - Get the `owid-covid-data.csv` file from [Our World in Data](https://ourworldindata.org/covid-cases)
   - Place the file in the same directory as your script or notebook

4. **Run the Python script or open the Jupyter Notebook** to view the visualizations.

---

## 📌 Key Insights

1. **India** had the highest total cases among the three countries by mid-2022.
2. **United States** showed the fastest and most extensive vaccine rollout.
3. **Kenya** experienced a slower rise in cases but a notable vaccination increase later.
4. **India’s death rate** spiked significantly during the mid-2021 wave.
5. **Vaccination trends improved globally** after the second quarter of 2021.

---

## 📁 File Structure

```
covid-analysis/
│
├── owid-covid-data.csv        # Source dataset (not included in repo)
├── covid_analysis.py          # Python script with data cleaning and visualization
├── README.md                  # Project documentation
└── (Optional) notebook.ipynb  # Jupyter Notebook version (if applicable)
```

---

## 🧠 Reflections

This project demonstrates how publicly available data can be used to understand health crises and inform public policy decisions. By comparing multiple countries, we gain a clearer picture of how responses and outcomes varied globally.
```
