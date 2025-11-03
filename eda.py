import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Replace 'your_file.csv' with the path to your CSV file
file_path = 'jobs_in_data.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(file_path)

''' EDA Begins here '''

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

''' Several relationships visualized with seaborn 
    the first two - Work Setting vs Salary and Geographic Region vs Salary we will
    explore further '''

# Set a consistent style
sns.set(style="whitegrid")

''' Work Setting vs Salary  '''

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="work_setting", y="salary_in_usd", palette="Set2")
plt.title("Salary Distribution by Work Setting", fontsize=14)
plt.xlabel("Work Setting")
plt.ylabel("Salary (USD)")
plt.xticks(rotation=15)
plt.show()

''' Average Salaries for top 10 and bottom 10 countries '''

# Calculate average salary by country
avg_salary_by_country = df.groupby('employee_residence')['salary_in_usd'].mean().sort_values(ascending=False)

# Top 10 countries
top_10 = avg_salary_by_country.head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_10.values, y=top_10.index, palette="viridis")
plt.title("Top 10 Countries by Average Salary", fontsize=14)
plt.xlabel("Average Salary (USD)")
plt.ylabel("Country")
plt.show()

# Bottom 10 countries
bottom_10 = avg_salary_by_country.tail(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=bottom_10.values, y=bottom_10.index, palette="magma")
plt.title("Bottom 10 Countries by Average Salary", fontsize=14)
plt.xlabel("Average Salary (USD)")
plt.ylabel("Country")
plt.show()

''' Salary by Job Title '''

plt.figure(figsize=(12, 6))
top_titles = df['job_title'].value_counts().index[:10]  # Top 10 job titles
sns.boxplot(data=df[df['job_title'].isin(top_titles)], x="job_title", y="salary_in_usd", palette="coolwarm")
plt.title("Salary Distribution for Top 10 Job Titles", fontsize=14)
plt.xlabel("Job Title")
plt.ylabel("Salary (USD)")
plt.xticks(rotation=45)
plt.show()

''' Pairplot for Key Variables '''
pairplot_cols = ["salary_in_usd", "work_year", "experience_level"]

g = sns.pairplot(df[pairplot_cols], hue="experience_level", palette="husl", height=4)
g.fig.subplots_adjust(top=0.95)
g.fig.suptitle("Pairplot of Salary, Year, and Experience Level", fontsize=14)
for ax in g.axes.flatten():
    ax.tick_params(axis='x', rotation=45)
    ax.tick_params(axis='y', rotation=0)
plt.show()

''' Salary by Experience Level '''

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="experience_level", y="salary_in_usd", palette="muted")
plt.title("Salary Distribution by Experience Level", fontsize=14)
plt.xlabel("Experience Level")
plt.ylabel("Salary (USD)")
plt.show()

''' Average Salary over years '''

plt.figure(figsize=(8, 6))
sns.lineplot(data=df, x="work_year", y="salary_in_usd", estimator="mean", ci=None, marker="o")
plt.title("Average Salary Trend Over Years", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Average Salary (USD)")
plt.show()
