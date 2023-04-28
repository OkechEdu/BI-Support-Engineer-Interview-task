import pandas as pd

# Load the data into a pandas dataframe
#df = pd.read_csv('sales_data.csv')
df = pd.read_excel('data_extract_sales_201612.xlsx')

# Calculate the total number of items sold for each transaction
df['total_items'] = df['QUANTITY']

# Group the data by product category and transaction number, and calculate the sum of total_items
grouped_df = df.groupby(['PRODUCT_CATEGORY_NAME', 'TRANSACTION_NUMBER']).agg({'total_items': 'sum'})

# Group the data by product category and calculate the mean of total_items
average_items_per_transaction = grouped_df.groupby(['PRODUCT_CATEGORY_NAME']).agg({'total_items': 'mean'})

# Print the result
print(average_items_per_transaction)
