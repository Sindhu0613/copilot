import pandas as pd
import os

# Load the main Excel sheet containing names
main_excel = pd.read_excel('C:\\Users\\Admin\\Documents\\names\\All_Names.xlsx')
column_name = 'TELUGU_NAMES'

# List all the other Excel files in the directory
directory = r'C:\\Users\\Admin\\Documents\\female_names'
all_files = os.listdir(directory)
other_excels = [file for file in all_files if file.endswith('.xlsx') and file != 'All_Names.xlsx']

# Compare names and create separate Excel files for each match
for excel_file in other_excels:
    excel_data = pd.read_excel(os.path.join(directory, excel_file))
    matching_names = main_excel[main_excel[column_name].isin(excel_data[column_name])]
    
    if not matching_names.empty:
        # Create a new Excel file for the matching names
        output_file = f'matching_{excel_file}'
        matching_names.to_excel(os.path.join(directory, output_file), index=False)
        print(f"Matching names found in {excel_file}. Saved to {output_file}.")
    else:
        print(f"No matching names found in {excel_file}.")
