# Import all required libraries
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

def load_and_prepare_data():
    """Load the dataset and perform initial preparation"""
    try:
        df = pd.read_csv('owid-covid-data.csv')
        print("Dataset successfully loaded!")
        
        # Convert date column to datetime format
        df['date'] = pd.to_datetime(df['date'])
        
        return df
    except FileNotFoundError:
        print("Error: File not found. Please ensure 'owid-covid-data.csv' is in your working directory.")
        return None

def clean_and_filter_data(df, countries_of_interest):
    """Clean and filter the dataset for analysis"""
    # Filter for countries of interest
    filtered_df = df[df['location'].isin(countries_of_interest)].copy()
    
    # Select relevant columns
    columns_to_keep = [
        'date', 'location', 'continent', 'iso_code', 'total_cases', 'new_cases', 
        'total_deaths', 'new_deaths', 'total_vaccinations', 'people_vaccinated', 
        'people_fully_vaccinated', 'population', 'life_expectancy', 'gdp_per_capita',
        'total_cases_per_million', 'total_deaths_per_million'
    ]
    filtered_df = filtered_df[columns_to_keep]
    
    # Handle missing values
    cols_to_fill_zero = [
        'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
        'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'
    ]
    filtered_df[cols_to_fill_zero] = filtered_df[cols_to_fill_zero].fillna(0)
    
    # Calculate derived metrics
    filtered_df['death_rate'] = filtered_df['total_deaths'] / filtered_df['total_cases']
    filtered_df['vaccination_rate'] = filtered_df['people_vaccinated'] / filtered_df['population']
    
    # Remove infinite values from death rate calculation
    filtered_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    return filtered_df

def plot_time_series(data, countries, metric, title, ylabel, log_scale=False):
    """Plot time series data for multiple countries"""
    plt.figure(figsize=(14, 8))
    for country in countries:
        country_data = data[data['location'] == country]
        sns.lineplot(data=country_data, x='date', y=metric, label=country)
    
    plt.title(title, fontsize=16)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.legend(title='Country')
    if log_scale:
        plt.yscale('log')
    plt.show()

def plot_comparison_bar(data, x_metric, y_metric, title, xlabel, palette='viridis'):
    """Plot comparative bar chart"""
    plt.figure(figsize=(14, 8))
    sns.barplot(data=data.sort_values(x_metric, ascending=False),
                x=x_metric, y=y_metric, palette=palette)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel)
    plt.ylabel('Country')
    plt.show()

def analyze_data(filtered_df, countries_of_interest):
    """Perform comprehensive data analysis and visualization"""
    # 1. Time Series Analysis
    plot_time_series(filtered_df, countries_of_interest, 'total_cases', 
                    'Total COVID-19 Cases Over Time', 'Total Cases', log_scale=True)
    
    # Plot new cases with 7-day rolling average
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
    
    # 2. Comparative Analysis
    latest_data = filtered_df.sort_values('date').groupby('location').last().reset_index()
    
    plot_comparison_bar(latest_data, 'total_cases', 'location', 
                       'Total COVID-19 Cases by Country', 'Total Cases')
    
    plot_comparison_bar(latest_data, 'death_rate', 'location', 
                       'COVID-19 Death Rates by Country', 'Death Rate (Deaths/Cases)', 'magma')
    
    # 3. Vaccination Analysis
    plot_time_series(filtered_df, countries_of_interest, 'vaccination_rate', 
                    'Vaccination Rates Over Time', 'Vaccination Rate')
    
    plot_comparison_bar(latest_data, 'vaccination_rate', 'location', 
                       'Current Vaccination Rates by Country', 'Vaccination Rate', 'rocket')
    
    # 4. Choropleth Map
    latest_global_data = df.sort_values('date').groupby('location').last().reset_index()
    
    fig = px.choropleth(latest_global_data,
                        locations="iso_code",
                        color="total_cases_per_million",
                        hover_name="location",
                        hover_data=["total_cases", "total_deaths"],
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="Global COVID-19 Cases per Million People",
                        labels={'total_cases_per_million': 'Cases per Million'})
    fig.show()
    
    return latest_data

def generate_insights(latest_data):
    """Generate and print key insights from the data"""
    print("\n=== KEY INSIGHTS ===")
    
    # Top countries by cases
    top_cases = latest_data.sort_values('total_cases', ascending=False).head(3)
    print(f"\n1. Countries with highest total cases: {', '.join(top_cases['location'].tolist())}")
    
    # Vaccination leaders
    top_vax = latest_data[latest_data['people_vaccinated'] > 0].sort_values('vaccination_rate', ascending=False).head(3)
    print(f"\n2. Vaccination leaders (highest rates): {', '.join(top_vax['location'].tolist())}")
    
    # Death rate analysis
    avg_death_rate = latest_data['death_rate'].mean()
    high_dr = latest_data[latest_data['death_rate'] > avg_death_rate].sort_values('death_rate', ascending=False).head(3)
    print(f"\n3. Countries with above-average death rates: {', '.join(high_dr['location'].tolist())}")
    
    # GDP correlation
    correlation = latest_data[['gdp_per_capita', 'vaccination_rate']].corr().iloc[0,1]
    print(f"\n4. Correlation between GDP per capita and vaccination rate: {correlation:.2f}")
    
    # Latest date in data
    latest_date = filtered_df['date'].max().strftime('%Y-%m-%d')
    print(f"\n5. Data current as of: {latest_date}")

# Main execution
if __name__ == "__main__":
    # Define countries of interest
    countries_of_interest = [
        'United States', 'India', 'Brazil', 'United Kingdom', 
        'Kenya', 'South Africa', 'Germany', 'Japan'
    ]
    
    # Load and prepare data
    df = load_and_prepare_data()
    if df is not None:
        # Clean and filter data
        filtered_df = clean_and_filter_data(df, countries_of_interest)
        
        # Perform analysis
        latest_data = analyze_data(filtered_df, countries_of_interest)
        
        # Generate insights
        generate_insights(latest_data)
        
        # Save processed data
        filtered_df.to_csv('processed_covid_data.csv', index=False)
        print("\nProcessed data saved to 'processed_covid_data.csv'")