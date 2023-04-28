import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm


# Load data into a DataFrame
df = pd.read_excel('data_extract_sales_201612.xlsx')

# Group by product category and transaction number
grouped = df.groupby(['PRODUCT_CATEGORY_NAME', 'TRANSACTION_NUMBER'])

# Calculate the number of unique items in each transaction
num_items = grouped['QUANTITY'].sum()

# Calculate the mean and standard deviation of the number of items per transaction
mean = num_items.mean()
std_dev = num_items.std()

# Calculate the Z-score for each transaction
z_scores = (num_items - mean) / std_dev

z_score = norm.ppf(0.05)
print(f'the Z-score value for the 5% cutoff point is: `{z_score}`')

# # Calculate the threshold for uncommon transactions
# threshold = stats.norm.ppf(0.95)

# # Categorize each transaction as either common or uncommon
# is_common = abs(z_scores) < threshold

# # Count the number of common and uncommon transactions for each category
# group_size = grouped.size()
# common_count = group_size[is_common].sum()
# uncommon_count = group_size[~is_common].sum()

# # Display the results
# print('Common transactions:\n', common_count)
# print('Uncommon transactions:\n', uncommon_count)