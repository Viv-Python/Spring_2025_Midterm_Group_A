import pandas as pd
from sklearn.preprocessing import  OrdinalEncoder, StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'jobs_in_data.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(file_path)

''' Encoding category variables for ordinal fields (those with order to them).
    This makes them numerical and easier for the model to handle 
    Also we are counting year as a category and not a numeric '''

# Ordinal columns (assumed to have order)
ordinal_cols = ['work_year','experience_level', 'employment_type', 'company_size']
ordinal_encoder = OrdinalEncoder()
df[ordinal_cols] = ordinal_encoder.fit_transform(df[ordinal_cols])


''' Checking for Multicollinearity. In short if there is a high correlation betwene our numerical columns.
    We use this to justify dropping one of our salary columns since there is a redundancy there'''

# pip install statsmodels (if needed)

salaries = ['salary', 'salary_in_usd']

X = df[salaries]
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)

# dropping salary column & salary_currency as they are redundant and salary_in_usd is more useful
df.drop('salary', axis=1, inplace=True)
df.drop('salary_currency', axis=1, inplace=True)


''' Feature scaling numeric fields - salary in usd'''

numeric_cols = ['salary_in_usd']

scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Save the pre-processed dataset
df.to_csv("jobs_pre_process.csv", index=False)
