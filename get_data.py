import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

# Authenticate with Kaggle
api = KaggleApi()
api.authenticate()

# Download the dataset
dataset = "hummaamqaasim/jobs-in-data"
download_path = "kaggle_data"
os.makedirs(download_path, exist_ok=True)
api.dataset_download_files(dataset, path=download_path, unzip=True)

# Load the CSV file
data_file = os.path.join(download_path, "jobs_in_data.csv")
df = pd.read_csv(data_file)



# Display information about the dataset
print("Dataset Information:")
print(df.info())

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Correct invalid entries (example: fill missing values)
df = df.fillna(method='ffill')

# Save the cleaned dataset
cleaned_data_file = os.path.join(download_path, "jobs_cleaned.csv")
df.to_csv(cleaned_data_file, index=False)

print("Path to cleaned dataset:", cleaned_data_file)

# Compute basic stats (mean, median, std, etc.).
#mean
mean_values = df.mean(numeric_only=True)
print("Mean Values:")
print(mean_values)

#median
median_values = df.median(numeric_only=True)
print("Median Values:")
print(median_values)

#std
std_values = df.std(numeric_only=True)
print("Standard Deviation Values:")
print(std_values)       
