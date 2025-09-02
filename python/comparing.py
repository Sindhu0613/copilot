import pandas as pd

# Load both Excel files into pandas DataFrames
first_excel = pd.read_excel(r'C:\\Users\\Admin\\Documents\\ibp data\\Final_Ibrahimpatnam_Pension.xlsx')
second_excel = pd.read_excel(r'C:\\Users\\Admin\\Documents\\ibp data\\ibt.xlsx', header=0)

second_excel = second_excel[~second_excel['Mobile '].isin(first_excel['B_MOBILE_NO'])]

second_excel.to_excel('matched.xlsx')
# Assuming 'Mobile Numbers' is the column name where you want to match the data
# Merge the two DataFrames based on the 'Mobile Numbers' column
#merged_data = pd.merge(first_excel, second_excel, on='Mobile', how='inner')

# Save the matched data to a separate Excel sheet
# with pd.ExcelWriter('matched_data_1.xlsx') as writer:
#     merged_data.to_excel(writer, index=False, sheet_name='Matched Data')
