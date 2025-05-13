import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from datetime import datetime, timedelta

def generate_mock_data():
    """Generate mock sales data for analysis"""
    # Create date range for past 30 days
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') 
             for i in range(30, 0, -1)]
    
    # Products with different sales patterns
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
    
    # Generate mock data
    data = []
    for date in dates:
        for product in products:
            # Base quantity with some randomness
            base_qty = {
                'Laptop': np.random.randint(1, 5),
                'Mouse': np.random.randint(5, 20),
                'Keyboard': np.random.randint(3, 10),
                'Monitor': np.random.randint(1, 4),
                'Headphones': np.random.randint(2, 8)
            }[product]
            
            # Add some date-based variation (e.g., more sales on weekends)
            day_of_week = datetime.strptime(date, '%Y-%m-%d').weekday()
            if day_of_week >= 5:  # Weekend
                base_qty = int(base_qty * 1.5)
            
            # Add some random fluctuation
            quantity = max(1, int(np.random.normal(base_qty, 2)))
            
            # Set prices
            prices = {
                'Laptop': 1000,
                'Mouse': 20,
                'Keyboard': 100,
                'Monitor': 300,
                'Headphones': 150
            }
            
            revenue = quantity * prices[product]
            
            data.append([date, product, quantity, revenue])
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Product', 'Quantity Sold', 'Revenue ($)'])
    return df

def analyze_sales_data(df):
    """Perform analysis on the sales data"""
    # Calculate total revenue
    total_revenue = df['Revenue ($)'].sum()
    
    # Find best-selling product
    best_selling = df.loc[df['Quantity Sold'].idxmax()]
    best_product = best_selling['Product']
    best_quantity = best_selling['Quantity Sold']
    
    # Identify day with highest sales (by revenue)
    df['Date'] = pd.to_datetime(df['Date'])
    daily_sales = df.groupby('Date')['Revenue ($)'].sum()
    highest_day = daily_sales.idxmax().strftime('%Y-%m-%d')
    highest_day_revenue = daily_sales.max()
    
    # Prepare insights text
    insights = f"""Sales Data Analysis Results:
----------------------------
Total Revenue: ${total_revenue:,.2f}
Best-Selling Product: {best_product} ({best_quantity} units sold)
Highest Sales Day: {highest_day} (${highest_day_revenue:,.2f} in revenue)

Top 5 Selling Products by Quantity:
"""
    
    # Add top products by quantity
    top_products = df.groupby('Product')['Quantity Sold'].sum().sort_values(ascending=False)
    for product, qty in top_products.head().items():
        insights += f"- {product}: {qty} units\n"
    
    # Save insights to file
    with open('sales_summary.txt', 'w') as f:
        f.write(insights)
    
    # Print insights to console
    print(insights)
    
    # Generate visualizations
    try:
        # Set style for plots
        plt.style.use('seaborn')
        
        # Daily revenue trend
        plt.figure(figsize=(12, 6))
        daily_sales.plot(kind='line', marker='o', color='royalblue', linewidth=2)
        plt.title('Daily Sales Revenue Trend', fontsize=14, pad=20)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Revenue ($)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('daily_revenue_trend.png', dpi=300)
        
        # Product sales by quantity
        plt.figure(figsize=(12, 6))
        top_products.plot(kind='barh', color='forestgreen')
        plt.title('Total Units Sold by Product', fontsize=14, pad=20)
        plt.xlabel('Quantity Sold', fontsize=12)
        plt.ylabel('Product', fontsize=12)
        plt.tight_layout()
        plt.savefig('product_sales_quantity.png', dpi=300)
        
        # Weekly sales pattern
        plt.figure(figsize=(12, 6))
        df['Weekday'] = df['Date'].dt.day_name()
        weekday_sales = df.groupby('Weekday')['Revenue ($)'].sum()
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_sales = weekday_sales.reindex(weekday_order)
        weekday_sales.plot(kind='bar', color='darkorange')
        plt.title('Weekly Sales Pattern', fontsize=14, pad=20)
        plt.xlabel('Day of Week', fontsize=12)
        plt.ylabel('Revenue ($)', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('weekly_sales_pattern.png', dpi=300)
        
        print("\nVisualizations saved:")
        print("- daily_revenue_trend.png")
        print("- product_sales_quantity.png")
        print("- weekly_sales_pattern.png")
    except Exception as e:
        print(f"\nCould not generate visualizations: {e}")

def main():
    print("Generating mock sales data...")
    df = generate_mock_data()
    
    print("\nAnalyzing sales data...")
    analyze_sales_data(df)
    
    # Save the mock data for reference
    df.to_csv('mock_sales_data.csv', index=False)
    print("\nMock data saved as 'mock_sales_data.csv'")

if __name__ == "__main__":
    main()