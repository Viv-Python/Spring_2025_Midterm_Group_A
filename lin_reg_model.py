import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

''' Here we will be testing the hypothesis that remote work pays more in general.
    There are three categories of work here: In-person, remote, and hyrbid.
    We will be using a linear regression model applied to the work_setting and salary_in_usd fields
    and then using the MAE and Coeffiecients to intepret that hypothesis. '''

# Load dataset
df = pd.read_csv("jobs_pre_process.csv")

# Feature selection
X = df[['work_setting']]
y = df['salary_in_usd']


''' Here hybrid will get dropped as a baseline '''
# One-hot encoding of 'work_setting'
encoder = OneHotEncoder(drop='first', sparse_output=False)
X_encoded = encoder.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Fit Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Extract coefficients
feature_names = encoder.get_feature_names_out(['work_setting'])
coefficients = model.coef_
coef_df = pd.DataFrame({
    'Work Setting': feature_names,
    'Coefficient': coefficients
})

# Output results
print("Linear Regression Coefficients for Work Setting:")
print(coef_df)
print("\nModel Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")