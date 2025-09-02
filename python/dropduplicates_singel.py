import pandas as pd
# Specify the input file
input_file = r'C:\\Users\\Admin\\Documents\\UNIQUES_NAMES_ALL_CONS\\Final_ALL_CONS.xlsx'
# Specify the output file
output_file = r'C:\\Users\\Admin\\Documents\\UNIQUES_NAMES_ALL_CONS.xlsx'
# Read the Excel file into a DataFrame
df = pd.read_excel(input_file)
# Remove duplicates from 'Unique_names' and 'Telugu_Unique_names'
df_unique = df.drop_duplicates(subset=['Unique_names', 'Telugu_Unique_names'])
# Save the unique DataFrame to a new Excel file
df_unique.to_excel(output_file, index=False)
print(f'Unique values saved to {output_file}')
