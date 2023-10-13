import numpy as np
import pandas as pd
data = pd.read_csv("D:/Enored/supermarket_sales - Sheet1.csv")
data
missing_values_count = data.isnull().sum()
missing_values_count
