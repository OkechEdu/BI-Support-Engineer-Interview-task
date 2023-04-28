import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# Load data into a DataFrame
df = pd.read_excel('data_extract_sales_201612.xlsx')

# Group by product category and transaction number
grouped = df.groupby(['PRODUCT_CATEGORY_NAME', 'TRANSACTION_NUMBER'])

# Calculate the number of unique items in each transaction
total_items_per_transaction = grouped['QUANTITY'].sum()

# Calculate the mean and standard deviation of the number of items per transaction
mean = total_items_per_transaction.mean()
std_dev = total_items_per_transaction.std()

# Calculate the Z-score for each transaction
z_scores = (total_items_per_transaction - mean) / std_dev

# Calculate the threshold for uncommon transactions
# threshold = stats.norm.ppf(0.95)

# Calculate the threshold using ZScore
threshold = np.mean(total_items_per_transaction) + 1.645 * np.std(total_items_per_transaction)

# Count the number of transactions where total items purchased are greater than the threshold
num_exceptions = len([i for i in total_items_per_transaction if i > threshold])

# Calculate the percentage of exceptions
percent_exceptions = num_exceptions / len(total_items_per_transaction) * 100

# Print the results
print("Number of exceptions:", num_exceptions)
print("Percentage of exceptions:", percent_exceptions)
