import pandas as pd

# Load the first Excel file
excel1 = pd.read_excel(r'C:\\Users\\Admin\\Documents\\ibp data\\ibrahimpatam_uniques.xlsx')

# Load the second Excel file
excel2 = pd.read_excel(r'C:\\Users\\Admin\\Documents\\ibp data\\filtered_data.xlsx')

# Name of the columns containing the names to match
column_name_excel1 = 'Names'
column_name_excel2 = 'Names'

# Perform the matching
matched_data = pd.merge(excel1, excel2, how='left', left_on=column_name_excel1, right_on=column_name_excel2)

# Extracting the matched data column
matched_column_name = 'Matched_Column_Name'
matched_data[matched_column_name] = matched_data[column_name_excel2]

# Save the result to a new Excel file
matched_data.to_excel('output_file.xlsx', index=False)
