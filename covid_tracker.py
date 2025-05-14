
# Analyzing COVID-19 trends using pandas, matplotlib, seaborn, and plotly

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Setup for plots
sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("owid-covid-data.csv")

# Filter for selected countries
countries = ['Kenya', 'USA', 'India']
df = df[df['location'].isin(countries)]

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Fill missing numeric values
df.fillna(0, inplace=True)

# Select relevant columns
columns = ['location', 'date', 'total_cases', 'new_cases', 'total_deaths',
           'new_deaths', 'total_vaccinations', 'people_fully_vaccinated']
df = df[columns]

# Plot total COVID-19 cases over time
plt.figure(figsize=(10, 5))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot daily new cases over time
plt.figure(figsize=(10, 5))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)

plt.title('Daily New COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.tight_layout()
plt.show()

# Calculate and plot death rate over time
df['death_rate'] = df['total_deaths'] / df['total_cases']
plt.figure(figsize=(10, 5))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)

plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.tight_layout()
plt.show()

# Plot vaccination progress
plt.figure(figsize=(10, 5))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.tight_layout()
plt.show()

# Choropleth map for latest total cases
latest = df[df['date'] == df['date'].max()]
fig = px.choropleth(
    latest,
    locations='location',
    locationmode='country names',
    color='total_cases',
    hover_name='location',
    color_continuous_scale='Inferno',
    title='Total COVID-19 Cases by Country (Latest)'
)
fig.show()
