
import kagglehub
import pandas as pd
import os

# Download latest version of the dataset
path = kagglehub.dataset_download("hummaamqaasim/jobs-in-data")

# Move dataset files to current directory
current_dir = os.getcwd()
for file_name in os.listdir(path):
    src = os.path.join(path, file_name)
    dst = os.path.join(current_dir, file_name)
    if os.path.isfile(src):
        os.replace(src, dst)

print("Dataset files moved to:", current_dir)

# Load the CSV file into a pandas DataFrame
csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
if csv_files:
    df = pd.read_csv(csv_files[0])
    print("First 5 rows of the dataset:")
    print(df.head())
else:
    print("No CSV files found in the dataset.")
