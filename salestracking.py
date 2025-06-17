import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales tracking data
sales_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [200, 220, 250, 270, 300, 320],
    'Expenses': [150, 160, 180, 200, 210, 230]
})

# Plotting sales and expenses over months
plt.figure(figsize=(8, 5))
sns.lineplot(data=sales_data, x='Month', y='Sales', marker='o', label='Sales')
sns.lineplot(data=sales_data, x='Month', y='Expenses', marker='o', label='Expenses')
plt.title('Sales and Expenses Tracking Over Months')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
