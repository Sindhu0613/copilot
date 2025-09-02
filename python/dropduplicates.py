import pandas as pd

# Read the Excel file
file_path = r'C:\\Users\\Admin\\Documents\\merge\\modified_namesfile.xlsx'
df = pd.read_excel(file_path)

# Remove duplicates from a specific column, for instance, column 'ColumnName'
column_name = 'Telugu_Unique_names'
df[column_name] = df[column_name].drop_duplicates()

# Save the updated DataFrame back to the Excel file
df.to_excel('final_Unique_Names_file.xlsx', index=False)
