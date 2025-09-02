import pandas as pd

# Load the Excel files
file1 = r'C:\\Users\\Admin\\Documents\\ibp data\\Final_Ibrahimpatnam_Pension.xlsx'
file2 = r'C:\\Users\\Admin\\Documents\\ibp data\\ibt.xlsx'

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Assuming mobile numbers are in columns named 'MobileNumber'
column_name = 'B_MOBILE_NO'

# Compare mobile numbers and extract matching rows
matching_rows = df1[df1['Mobile' ].isin(df2['B_MOBILE_NO'])]

# Save matching rows to a new Excel file
matching_rows.to_excel('matching_mobile_numbers.xlsx', index=False)
