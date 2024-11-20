import pandas as pd

# Load the CSV file
file_path = 'your_file.csv'  # Replace with your CSV file's path
df = pd.read_csv(file_path)

# Quick overview of the data
print("First 5 rows of the dataset:")
print(df.head())

print("\nSummary of the dataset:")
print(df.info())

print("\nBasic statistics of numeric columns:")
print(df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Get unique values for categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    print(f"\nUnique values in {column}:")
    print(df[column].unique())

# Generate some insights
print("\nInsights:")

# Example: Count occurrences of a column
if 'Category' in df.columns:  # Replace 'Category' with your column name
    print("\nCategory distribution:")
    print(df['Category'].value_counts())

# Example: Calculate correlation between numeric columns
if len(df.select_dtypes(include='number').columns) > 1:
    print("\nCorrelation between numeric columns:")
    print(df.corr())

# Example: Group by and aggregate
if 'Date' in df.columns and 'Value' in df.columns:  # Replace with relevant columns
    df['Date'] = pd.to_datetime(df['Date'])
    grouped = df.groupby(df['Date'].dt.year)['Value'].sum()
    print("\nYearly summary of 'Value':")
    print(grouped)

# Optional: Save the insights to a new CSV
output_path = 'insights.csv'
grouped.to_csv(output_path)
print(f"\nInsights saved to {output_path}")
