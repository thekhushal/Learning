import pandas as pd

# Load the CSV file
file_path = 'newdata.csv'  # Replace with your CSV file's path
df = pd.read_csv("/home/theta/CODE/Learning/Python_Regex/newdata.csv")


# print("General info about the DataFrame: ", df.info())  # General info about the DataFrame
# print("Statistical summary for numerical columns: ", df.describe())  # Statistical summary for numerical column
# print("Shape of data: (rows, columns) ", df.shape)  # Get number of rows and columns (rows, columns)
# print("List of column names: ", df.columns)  # List of column names
print(df.tail())  # Select the first 5 rows