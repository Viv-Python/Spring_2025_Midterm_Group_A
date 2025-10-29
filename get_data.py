import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("hummaamqaasim/jobs-in-data")

print("Path to dataset files:", path)