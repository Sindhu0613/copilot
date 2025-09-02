import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel(r'C:\\Users\\SriramineniSindu\\Documents\\data\\new2\\Guntur_West_unique2_completed.xlsx')

# Assuming the mobile numbers are in a column named 'MobileNumber', you can add '91' to each number
df['Mobile'] = '91' + df['Mobile'].astype(str)

# Save the modified DataFrame back to Excel
df.to_excel('modified_excel_file.xlsx', index=False)
