import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_explore_dataset(file_path):
    """
    Task 1: Load and Explore the Dataset
    - Loads the dataset from CSV file
    - Displays basic information about the dataset
    - Handles missing values
    - Returns cleaned DataFrame or None if error occurs
    """
    try:
        # Load the dataset
        print(f"\nLoading dataset from: {file_path}")
        df = pd.read_csv(file_path)
        
        # Display first 5 rows
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        
        # Show summary statistics
        print("\nSummary statistics:")
        print(df.describe())
        
        # Display dataset info (data types, non-null counts)
        print("\nDataset info:")
        print(df.info())
        
        # Check for missing values
        missing_values = df.isnull().sum()
        print("\nMissing values in each column:")
        print(missing_values)
        
        # Handle missing values if any exist
        if missing_values.any():
            print("\nHandling missing values...")
            for col in df.columns:
                if df[col].isnull().any():
                    # Fill numerical columns with mean
                    if pd.api.types.is_numeric_dtype(df[col]):
                        mean_val = df[col].mean()
                        df[col].fillna(mean_val, inplace=True)
                        print(f"Filled missing values in {col} with mean: {mean_val:.2f}")
                    # Fill categorical columns with mode
                    else:
                        mode_val = df[col].mode()[0]
                        df[col].fillna(mode_val, inplace=True)
                        print(f"Filled missing values in {col} with mode: {mode_val}")
        else:
            print("\nNo missing values found.")
        
        return df
    
    except FileNotFoundError:
        print(f"\nError: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("\nError: The file is empty.")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return None


def basic_data_analysis(df):
    """
    Task 2: Basic Data Analysis
    - Computes basic statistics
    - Performs grouping operations
    - Identifies patterns in the data
    """
    if df is None:
        print("\nDataframe is None, skipping analysis.")
        return
    
    # Show basic statistics for numerical columns
    print("\nBasic statistics of numerical columns:")
    print(df.describe())
    
    # Group by Species if column exists
    if 'Species' in df.columns:
        print("\nMean of numerical columns grouped by Species:")
        group_means = df.groupby('Species').mean()
        print(group_means)
        
        # Identify patterns in the grouped data
        print("\nKey findings from grouped analysis:")
        for col in group_means.columns:
            max_species = group_means[col].idxmax()
            max_value = group_means[col].max()
            min_species = group_means[col].idxmin()
            min_value = group_means[col].min()
            
            print(f"\nFor {col}:")
            print(f"- '{max_species}' has the highest mean value: {max_value:.2f}")
            print(f"- '{min_species}' has the lowest mean value: {min_value:.2f}")
            print(f"- Range: {max_value - min_value:.2f}")
    else:
        print("\nNo 'Species' column found for grouping.")


def data_visualization(df):
    """
    Task 3: Data Visualization
    Creates 4 types of plots:
    1. Line chart showing trend across samples
    2. Bar chart comparing values across categories
    3. Histogram showing distribution
    4. Scatter plot showing relationship between two variables
    """
    if df is None:
        print("\nDataframe is None, skipping visualization.")
        return
    
    # Set style for all plots
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 1. Line chart - Sepal Length trend across samples
    plt.subplot(2, 2, 1)
    plt.plot(df.index, df['SepalLengthCm'], color='blue', marker='o', linestyle='-', markersize=4)
    plt.title('Sepal Length Across Samples')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    
    # 2. Bar chart - Average Petal Length per Species
    plt.subplot(2, 2, 2)
    sns.barplot(x='Species', y='PetalLengthCm', data=df, ci=None, palette='viridis')
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Avg Petal Length (cm)')
    
    # 3. Histogram - Distribution of Sepal Width
    plt.subplot(2, 2, 3)
    plt.hist(df['SepalWidthCm'], bins=15, color='green', edgecolor='black', alpha=0.7)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    
    # 4. Scatter plot - Sepal Length vs Petal Length by Species
    plt.subplot(2, 2, 4)
    sns.scatterplot(x='SepalLengthCm', y='PetalLengthCm', hue='Species', 
                    data=df, palette='Set1', s=80, alpha=0.8)
    plt.title('Sepal vs Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adjust layout and display plots
    plt.tight_layout()
    plt.show()


def main():
    """Main function to execute all tasks"""
    # File path to Iris dataset
    file_path = 'week7/Iris.csv'
    
    # Task 1: Load and explore dataset
    iris_df = load_and_explore_dataset(file_path)
    
    # Task 2: Perform basic data analysis
    basic_data_analysis(iris_df)
    
    # Task 3: Create visualizations
    data_visualization(iris_df)


if __name__ == "__main__":
    main()