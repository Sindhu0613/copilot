import pandas as pd

# Read the Excel file
file_path = r'C:\\Users\\Admin\\Documents\\merge\\Telangana_Unique_Names.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Specify the column where you want to replace double spaces with single space
column_to_fix1 = 'Telugu_Unique_names'  # Replace with your column name
column_to_fix2 = 'Unique_names'
# Remove double spaces and replace with single space
df[column_to_fix1] = df[column_to_fix1].str.replace(r'\s+', ' ', regex=True)
df[column_to_fix2] = df[column_to_fix2].str.replace(r'\s+', ' ', regex=True)
# Save the modified DataFrame back to Excel
df.to_excel('modified_file.xlsx', index=False)  # Change the file name as needed
