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

