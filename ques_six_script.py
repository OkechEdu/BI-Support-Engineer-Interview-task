from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
import pandas as pd
from scipy import stats

# Load the data
df = pd.read_excel('data_extract_sales_201612.xlsx')

# Calculate the average number of items per transaction for each category
avg_items = df.groupby('PRODUCT_CATEGORY_NAME')['QUANTITY'].mean()

# Calculate the average number of unique items per transaction for each category
grouped = df.groupby(['PRODUCT_CATEGORY_NAME', 'TRANSACTION_NUMBER'])
unique_items = grouped['PRODUCT_CATEGORY_KEY'].nunique().groupby('PRODUCT_CATEGORY_NAME').mean()

# Categorize transactions as common or uncommon
num_items = grouped['QUANTITY'].sum()
mean = num_items.mean()
std_dev = num_items.std()
z_scores = (num_items - mean) / std_dev
threshold = stats.norm.ppf(0.95)
is_common = abs(z_scores) < threshold
group_size = grouped.size()
common_count = group_size[is_common].sum()
uncommon_count = group_size[~is_common].sum()

# Create a PDF canvas
pdf_file = 'sales_report-Edward-Okech.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter)
story = []

#main title
head_title = 'Sales Report - December 2016'
story.append(Table([[head_title]]))
story.append(Spacer(1, inch/2))

# Add title for question 1
title_1 = 'Average Number of Items per Transaction by Product Category'
story.append(Spacer(1, inch/2))
story.append(Table([[title_1]]))
story.append(Spacer(1, inch/4))

# Create a table of the results for question 1
table_data_1 = [['Product Category Name', 'Average Number of Items per Transaction']]
for category, avg in avg_items.items():
    table_data_1.append([category, f'{avg:.2f}'])

# Define the table style for question 1
style_1 = [
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightskyblue),
    ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER')
]

# Create the table object for question 1
table_1 = Table(table_data_1)
table_1.setStyle(TableStyle(style_1))
story.append(table_1)
story.append(Spacer(1, inch/2))

# Add title for question 2
title_2 = 'Average Number of Unique Items per Transaction by Product Category'
story.append(Table([[title_2]]))
story.append(Spacer(1, inch/4))

# Create a table of the results for question 2
table_data_2 = [['Product Category Name', 'Average Number of Unique Items per Transaction']]
for category, avg in unique_items.items():
    table_data_2.append([category, f'{avg:.2f}'])

# Define the table style for question 2
style_2 = [
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.indianred),
    ('BACKGROUND', (0, 1), (-1, 1), colors.lightcoral),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER')
]

# Create the table object for question 2
table_2 = Table(table_data_2)
table_2.setStyle(TableStyle(style_2))
story.append(table_2)
story.append(Spacer(1, inch/2))

# Add title for question 2
title_3 = 'How many transactions are classified as uncommon and common?'
story.append(Table([[title_3]]))
story.append(Spacer(1, inch/4))

# Create a table of the results for question 3
table_data_3 = [['Transaction Type', 'Count']]
table_data_3.append(['Common Transactions', common_count])
table_data_3.append(['Uncommon Transactions', uncommon_count])

# Define the table style for question 3
style_3 = [
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightseagreen),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER')
]
table_3 = Table(table_data_3)
table_3.setStyle(TableStyle(style_3))
story.append(table_3)


doc.build(story)

print('PDF report generated successfully.')




