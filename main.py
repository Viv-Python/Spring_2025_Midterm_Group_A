
import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'jobs_in_data.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(file_path)

# Print the entire DataFrame
print(df)

# (Optional) Print the first 5 rows
print(df.head())
