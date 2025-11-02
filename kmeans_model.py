import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt

''' Here we are doing a KMeans clustering on the country and salaries (in usd).
    We used the measures of inertia and silhoutee to measure the effectiveness of our clusters.
    We used 5 clusters which gave a good trade off between inertia and silhoutte.
    Then we visualizes the clusters with a scatter plot.
    Then plotted the top 3 paying countries, bottom 3 and USA, Can, UK, and Aus for comparision '''

# Load the dataset
df = pd.read_csv("jobs_pre_process.csv")

# Encode the 'employee_residence' column
le = LabelEncoder()
df['employee_residence_encoded'] = le.fit_transform(df['employee_residence'])

# Prepare the features for clustering
X = df[['employee_residence_encoded', 'salary_in_usd']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Calculate inertia and silhouette score
inertia = kmeans.inertia_
silhouette = silhouette_score(X, df['cluster'])
print(f"Inertia: {inertia}")
print(f"Silhouette Score: {silhouette}")

# Scatter plot of clusters using Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='employee_residence_encoded', y='salary_in_usd', hue='cluster', palette='tab10')
plt.title('KMeans Clustering of Employee Residence and Scaled Salary')
plt.xlabel('Encoded Residence')
plt.ylabel('Scaled Salary')
plt.tight_layout()
plt.show()

# Compute average salary per country
avg_salary_by_country = df.groupby('employee_residence')['salary_in_usd'].mean().sort_values(ascending=False)

# Identify top 3 and bottom 3 countries by average salary
top_3 = avg_salary_by_country.head(3).index.tolist()
bottom_3 = avg_salary_by_country.tail(3).index.tolist()
specific_countries = ['United States', 'Canada', 'United Kingdom', 'Australia']

# Combine all countries of interest
countries_of_interest = list(set(top_3 + bottom_3 + specific_countries))

# Create a DataFrame for plotting
plot_df = avg_salary_by_country[countries_of_interest].sort_values(ascending=False).reset_index()
plot_df.columns = ['employee_residence', 'avg_salary']

# Assign colors
def assign_color(country):
    if country in top_3:
        return 'green'
    elif country in bottom_3:
        return 'red'
    else:
        return 'blue'

plot_df['color'] = plot_df['employee_residence'].apply(assign_color)

# Create bar chart using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=plot_df, x='employee_residence', y='avg_salary', palette=list(plot_df['color']))
plt.title('Average Scaled Salary by Country (Top 3, Bottom 3, and Selected)')
plt.xlabel('Country')
plt.ylabel('Scaled Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()