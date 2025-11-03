import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'jobs_in_data.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(file_path)

# Print the entire DataFrame
print(df)

# (Optional) Print the first 5 rows
print(df.head())

# Display information about the dataset
print("Dataset Information:")
print(df.info())
print("Dataset Description:")
print(df.describe())

''' These are just to show what cleaning steps would look like since there are no missing values in this dataset
    as well as no nulls, ie, no need for imputation  '''

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Correct invalid entries (example: fill missing values)
df = df.fillna(method='ffill')

# Save the cleaned dataset
df.to_csv("jobs_cleaned.csv", index=False) 