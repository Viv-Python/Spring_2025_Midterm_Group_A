import shutil

import kagglehub
import pandas as pd
import os
# Download latest version
import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("hummaamqaasim/jobs-in-data")
file_name = [i for i in os.listdir(path) if i.endswith(".csv")][0]
org_file_path = os.path.join(path, file_name)
cur_file_path = os.path.join(os.getcwd(), file_name)

shutil.copy(org_file_path, cur_file_path)
data_df = pd.read_csv(cur_file_path)
print(data_df)