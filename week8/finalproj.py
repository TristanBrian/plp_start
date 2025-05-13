"""
COVID-19 Global Data Tracker
===========================

A comprehensive analysis of global COVID-19 trends including cases, deaths, and vaccinations.

Project Objectives:
- Import and clean COVID-19 global data
- Analyze time trends (cases, deaths, vaccinations)
- Compare metrics across countries/regions
- Visualize trends with charts and maps
- Communicate findings with narrative insights

Data Source: Our World in Data COVID-19 Dataset (owid-covid-data.csv)
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

def load_and_explore_data():
    """
    Load the dataset and perform initial exploration
    Meets Requirements:
    - Data Collection (Step 1)
    - Data Loading & Exploration (Step 2)
    """
    print("=== DATA LOADING & EXPLORATION ===")
    
    try:
        # Load the dataset
        df = pd.read_csv('owid-covid-data.csv')
        print("✅ Dataset successfully loaded!")
        
        # Basic exploration
        print("\n=== Dataset Structure ===")
        print(f"Shape: {df.shape} (rows, columns)")
        
        print("\n=== Column Names ===")
        print(df.columns.tolist())
        
        print("\n=== Sample Data ===")
        print(df.head())
        
        print("\n=== Missing Values Summary ===")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0].sort_values(ascending=False))
        
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        print(f"\nDate range: {df['date'].min().date()} to {df['date'].max().date()}")
        
        return df
    
    except FileNotFoundError:
        print("❌ Error: File not found. Please ensure 'owid-covid-data.csv' is in your working directory.")
        return None

def clean_and_prepare_data(df, countries_of_interest):
    """
    Clean and prepare the data for analysis
    Meets Requirements:
    - Data Cleaning (Step 3)
    """
    print("\n=== DATA CLEANING ===")
    
    # Filter for countries of interest
    filtered_df = df[df['location'].isin(countries_of_interest)].copy()
    print(f"Filtered data for {len(countries_of_interest)} countries.")
    
    # Select relevant columns
    key_columns = [
        'date', 'location', 'continent', 'iso_code', 
        'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
        'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
        'population', 'total_cases_per_million', 'total_deaths_per_million'
    ]
    filtered_df = filtered_df[key_columns]
    
    # Handle missing values
    print("\nHandling missing values:")
    cases_deaths_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths']
    vax_cols = ['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']
    
    # Fill cases/deaths with 0 (assuming missing means no cases)
    filtered_df[cases_deaths_cols] = filtered_df[cases_deaths_cols].fillna(0)
    print(f"- Filled {cases_deaths_cols} with 0 where missing")
    
    # For vaccination data, forward fill then fill remaining with 0
    filtered_df[vax_cols] = filtered_df.groupby('location')[vax_cols].ffill().fillna(0)
    print(f"- Forward filled vaccination data, then filled remaining with 0")
    
    # Calculate derived metrics
    filtered_df['death_rate'] = filtered_df['total_deaths'] / filtered_df['total_cases']
    filtered_df['vaccination_rate'] = filtered_df['people_vaccinated'] / filtered_df['population']
    
    # Clean infinite values from division
    filtered_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    print("\n✅ Data cleaning complete!")
    return filtered_df

def perform_eda(filtered_df, countries_of_interest):
    """
    Perform exploratory data analysis with visualizations
    Meets Requirements:
    - Exploratory Data Analysis (Step 4)
    - Visualizing Vaccination Progress (Step 5)
    """
    print("\n=== EXPLORATORY DATA ANALYSIS ===")
    
    # 1. Time Series Analysis
    print("\nVisualizing time trends...")
    
    # Total Cases Over Time
    plt.figure(figsize=(14, 8))
    for country in countries_of_interest:
        country_data = filtered_df[filtered_df['location'] == country]
        sns.lineplot(data=country_data, x='date', y='total_cases', label=country)
    plt.title('Total COVID-19 Cases Over Time', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Total Cases (log scale)')
    plt.yscale('log')
    plt.legend(title='Country')
    plt.show()
    
    # New Cases (7-day average)
    plt.figure(figsize=(14, 8))
    for country in countries_of_interest:
        country_data = filtered_df[filtered_df['location'] == country]
        country_data['new_cases_7day_avg'] = country_data['new_cases'].rolling(7).mean()
        sns.lineplot(data=country_data, x='date', y='new_cases_7day_avg', label=country)
    plt.title('Daily New Cases (7-day Moving Average)', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.legend(title='Country')
    plt.show()
    
    # 2. Death Analysis
    print("\nAnalyzing death rates...")
    
    # Total Deaths Over Time
    plt.figure(figsize=(14, 8))
    for country in countries_of_interest:
        country_data = filtered_df[filtered_df['location'] == country]
        sns.lineplot(data=country_data, x='date', y='total_deaths', label=country)
    plt.title('Total COVID-19 Deaths Over Time', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.legend(title='Country')
    plt.show()
    
    # Death Rate Comparison
    latest_data = filtered_df.sort_values('date').groupby('location').last().reset_index()
    plt.figure(figsize=(14, 8))
    sns.barplot(data=latest_data.sort_values('death_rate', ascending=False),
                x='death_rate', y='location', palette='magma')
    plt.title('COVID-19 Death Rates by Country', fontsize=16)
    plt.xlabel('Death Rate (Deaths/Cases)')
    plt.ylabel('Country')
    plt.show()
    
    # 3. Vaccination Analysis
    print("\nAnalyzing vaccination progress...")
    
    # Vaccination Rates Over Time
    plt.figure(figsize=(14, 8))
    for country in countries_of_interest:
        country_data = filtered_df[filtered_df['location'] == country]
        sns.lineplot(data=country_data, x='date', y='vaccination_rate', label=country)
    plt.title('Vaccination Rates Over Time', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Vaccination Rate (People Vaccinated/Population)')
    plt.legend(title='Country')
    plt.show()
    
    # Current Vaccination Status
    plt.figure(figsize=(14, 8))
    sns.barplot(data=latest_data.sort_values('vaccination_rate', ascending=False),
                x='vaccination_rate', y='location', palette='rocket')
    plt.title('Current Vaccination Rates by Country', fontsize=16)
    plt.xlabel('Vaccination Rate')
    plt.ylabel('Country')
    plt.show()
    
    return latest_data

def create_choropleth_map(df):
    """
    Create a choropleth map visualization
    Meets Requirements:
    - Optional: Build a Choropleth Map (Step 6)
    """
    print("\n=== CREATING CHOROPLETH MAP ===")
    
    # Prepare latest global data
    latest_global_data = df.sort_values('date').groupby('location').last().reset_index()
    
    # Create the map
    fig = px.choropleth(latest_global_data,
                        locations="iso_code",
                        color="total_cases_per_million",
                        hover_name="location",
                        hover_data=["total_cases", "total_deaths", "people_vaccinated"],
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="Global COVID-19 Cases per Million People",
                        labels={'total_cases_per_million': 'Cases per Million'})
    
    print("✅ Choropleth map created!")
    fig.show()

def generate_insights_report(latest_data, filtered_df):
    """
    Generate and display key insights from the analysis
    Meets Requirements:
    - Insights & Reporting (Step 7)
    """
    print("\n=== KEY INSIGHTS REPORT ===")
    
    # Get the latest date in the data
    latest_date = filtered_df['date'].max().strftime('%B %d, %Y')
    
    print(f"\nCOVID-19 Global Trends Analysis - Report as of {latest_date}")
    print("="*60)
    
    # 1. Cases Analysis
    top_cases = latest_data.sort_values('total_cases', ascending=False).head(3)
    print("\n1. TOP COUNTRIES BY TOTAL CASES:")
    for i, row in top_cases.iterrows():
        print(f"   {row['location']}: {int(row['total_cases']):,} cases")
    
    # 2. Death Rate Analysis
    high_death_rate = latest_data[latest_data['death_rate'] > 0].sort_values('death_rate', ascending=False).head(3)
    print("\n2. HIGHEST DEATH RATES (deaths/cases):")
    for i, row in high_death_rate.iterrows():
        print(f"   {row['location']}: {row['death_rate']:.2%}")
    
    # 3. Vaccination Analysis
    high_vax = latest_data[latest_data['vaccination_rate'] > 0].sort_values('vaccination_rate', ascending=False).head(3)
    low_vax = latest_data[latest_data['vaccination_rate'] > 0].sort_values('vaccination_rate').head(3)
    
    print("\n3. VACCINATION PROGRESS:")
    print("   Leaders in vaccination rates:")
    for i, row in high_vax.iterrows():
        print(f"   {row['location']}: {row['vaccination_rate']:.1%} vaccinated")
    
    print("\n   Countries with lowest vaccination rates:")
    for i, row in low_vax.iterrows():
        print(f"   {row['location']}: {row['vaccination_rate']:.1%} vaccinated")
    
    # 4. Case Fatality Trends
    print("\n4. CASE FATALITY TRENDS:")
    global_avg_death_rate = latest_data['death_rate'].mean()
    print(f"   Global average death rate: {global_avg_death_rate:.2%}")
    
    # 5. Interesting Patterns
    print("\n5. INTERESTING PATTERNS:")
    max_new_cases = filtered_df.loc[filtered_df['new_cases'].idxmax()]
    print(f"   Highest single-day case spike: {max_new_cases['location']} on {max_new_cases['date'].date()} ({int(max_new_cases['new_cases']):,} cases)")

def main():
    """
    Main function to execute the COVID-19 analysis pipeline
    """
    # Define countries of interest
    countries_of_interest = [
        'United States', 'India', 'Brazil', 'United Kingdom',
        'Germany', 'South Africa', 'Kenya', 'Japan'
    ]
    
    # Execute analysis pipeline
    print("="*60)
    print("COVID-19 GLOBAL DATA TRACKER")
    print("="*60)
    
    # 1. Load and explore data
    df = load_and_explore_data()
    if df is None:
        return
    
    # 2. Clean and prepare data
    filtered_df = clean_and_prepare_data(df, countries_of_interest)
    
    # 3. Perform EDA
    latest_data = perform_eda(filtered_df, countries_of_interest)
    
    # 4. Create choropleth map
    create_choropleth_map(df)
    
    # 5. Generate insights report
    generate_insights_report(latest_data, filtered_df)
    
    # 6. Save processed data
    filtered_df.to_csv('processed_covid_data.csv', index=False)
    print("\n✅ Analysis complete! Processed data saved to 'processed_covid_data.csv'")

if __name__ == "__main__":
    main()