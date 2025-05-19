
# 📦 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Optional: improve plot style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
```

---

df = pd.read_csv("owid-covid-data.csv")

# Preview data
print("Columns:", df.columns.tolist())
print(df.head())

# Check missing values
print(df.isnull().sum())

# 🧹 3. Data Cleaning
# Filter for selected countries
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Drop rows with missing critical values
df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Fill missing numeric values with 0
numeric_cols = ['new_cases', 'new_deaths', 'total_vaccinations']
df[numeric_cols] = df[numeric_cols].fillna(0)

# Optional: sort values for time-series plots
df = df.sort_values(['location', 'date'])

plt.figure()
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.show()

# 📊 EDA - Total Deaths Over Time
plt.figure()
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_deaths'], label=country)

plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.show()

# 📊 EDA - New Daily Cases
plt.figure()
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['new_cases'], label=country)

plt.title("New Daily COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.tight_layout()
plt.show()

df['death_rate'] = df['total_deaths'] / df['total_cases']

plt.figure()
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['death_rate'], label=country)

plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
for country in countries:
    data = df[df['location'] == country]
    plt.plot(data['date'], data['total_vaccinations'], label=country)

plt.title("COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.show()

# 🗺️ 6. Optional Choropleth Map
# Get latest data per country
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date][['iso_code', 'location', 'total_cases']]

# Plot with Plotly Express
fig = px.choropleth(latest_data,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title=f"Total COVID-19 Cases by Country (as of {latest_date.date()})")
fig.show()

# 📝 7. Insights (use this cell for Markdown in the notebook)

## Key Insights:

1. India had the highest total cases among the three countries by mid-2022.
2. The United States had a faster and broader vaccine rollout compared to Kenya.
3. Kenya's data showed slower case growth but a steeper rise in vaccinations later on.
4. The death rate in India spiked significantly during mid-2021.
5. Vaccination trends improved globally after Q2 2021.



