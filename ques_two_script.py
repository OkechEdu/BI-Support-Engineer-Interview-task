import pandas as pd

# Load the data into a pandas dataframe
#df = pd.read_csv('sales_data.csv')
df = pd.read_excel('data_extract_sales_201612.xlsx')

# Calculate the total number of items sold for each transaction
df['total_items'] = df['QUANTITY']

# # group by category and transaction number
# grouped = df.groupby(['PRODUCT_CATEGORY_NAME', 'TRANSACTION_NUMBER'])

# # count the unique items for each transaction and get the mean
# avg_unique_items = grouped['QUANTITY'].nunique().mean(level=0)

# Calculate the average unique items per transaction for each category
avg_unique_items_per_category = df.groupby('PRODUCT_CATEGORY_NAME')[['TRANSACTION_NUMBER', 'QUANTITY']].apply(
    lambda x: x.drop_duplicates(subset=['TRANSACTION_NUMBER'])['QUANTITY'].mean())


# Print the results
print("Average unique items per transaction for each category:")
print(avg_unique_items_per_category)


# # display the result
# print(avg_unique_items)
