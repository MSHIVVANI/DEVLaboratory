import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset from seaborn
titanic = sns.load_dataset('titanic')

# Display first 5 rows of original dataset
print("Original data (wide format):")
print(titanic.head())

# Reshaping with melt()
melted = pd.melt(
    titanic.reset_index(),
    id_vars=['index', 'class', 'sex'],
    value_vars=['age', 'fare', 'survived']
)
print("\nMelted data (long format):")
print(melted.head())

# Pivoting back to wide format
pivoted = melted.pivot(index='index', columns='variable', values='value').reset_index()
# Merge pivoted data with class and sex
pivoted = pivoted.merge(titanic[['class', 'sex']], left_on='index', right_index=True)
print("\nPivoted data (wide format):")
print(pivoted.head())

# Bar chart: Average fare by passenger class
avg_fare = titanic.groupby('class')['fare'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='class', y='fare', data=avg_fare)
plt.title('Average Fare by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Average Fare')
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.close()

# Heatmap: Correlation matrix of numeric variables
corr = titanic[['survived', 'pclass', 'age', 'fare']].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('heatmap.png')
plt.close()
