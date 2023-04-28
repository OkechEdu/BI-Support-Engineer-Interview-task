import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Create a sample dataframe
df = pd.DataFrame({
    'Product Category Name': ['Category 1', 'Category 1', 'Category 2', 'Category 2', 'Category 2'],
    'Item Name': ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'],
    'Price': [10.99, 20.99, 30.99, 40.99, 50.99]
})

# Create a table object from the dataframe
table_data = [df.columns.values.tolist()] + df.values.tolist()
table = Table(table_data)

# Define the table style
style = [
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER')
]

# Apply the table style
table.setStyle(TableStyle(style))

# Create a PDF file
pdf_file = 'report.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Add the table to the PDF file
story = []
story.append(table)
doc.build(story)

print('PDF report generated successfully.')
