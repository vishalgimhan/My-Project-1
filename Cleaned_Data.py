import numpy as np
import pandas as pd
data = pd.read_csv("D:/Enored/supermarket_sales - Sheet1.csv")
data
missing_values_count = data.isnull().sum()
missing_values_count

# Select the sales income column
sales_income = data['Total']

# Apply min-max normalization
min_sales_income = sales_income.min()
max_sales_income = sales_income.max()
normalized_sales_income = (sales_income - min_sales_income) / (max_sales_income - min_sales_income)

# Create a new column for the normalized values
data['normalized_sales_income'] = normalized_sales_income

import matplotlib.pyplot as plt
# Select the normalized sales income column
normalized_sales_income = data['normalized_sales_income']
# Create a bar chart
plt.bar(data.index, normalized_sales_income)

# Add a title and labels for the x and y axes
plt.title('Normalized Sales Income')
plt.xlabel('Sales')
plt.ylabel('Range')

# Adjust the size of the chart
plt.figure(figsize=(8, 6))

# Show the chart
plt.show()


# Identify duplicate rows
duplicate_rows = data[data.duplicated()]

# Display duplicate rows
print("Duplicate Rows except first occurrence:")
print(duplicate_rows)

import seaborn as sns

# Boxplot for 'Total' sales
sns.boxplot(x=data['Total'])
plt.show()





