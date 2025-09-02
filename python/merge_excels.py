#import pandas as pd

# Load the Excel files into Pandas DataFrames
#file1 = pd.read_excel(r'C:\\Users\\Admin\\Documents\\UNIQUES_NAMES_ALL_CONS\\ibrahimpatam_uniques.xlsx')
#file2 = pd.read_excel(r'C:\Users\\Admin\\Documents\\UNIQUES_NAMES_ALL_CONS\\Karimnagar_uniques.xlsx')
#file3 = pd.read_excel(r'C:\Users\\Admin\\Documents\\UNIQUES_NAMES_ALL_CONS\\Quthbullapur_uniques.xlsx')
#file4 = pd.read_excel(r'C:\Users\\Admin\\Documents\\UNIQUES_NAMES_ALL_CONS\\Sanathnagar_Uniques.xlsx')
# Merge the two DataFrames
#merged = pd.concat([file1, file2, file3, file4], ignore_index=True)

# Write the merged data to a new Excel file
#merged.to_excel('Final_ALL_CONS.xlsx', index=False)
import os
import pandas as pd

# Directory containing the Excel files
directory_path = r'C:\\Users\\Admin\\Documents\\female_names'

# Get all Excel files in the directory
excel_files = [file for file in os.listdir(directory_path) if file.endswith('.xlsx')]

# Initialize an empty list to store DataFrames
dfs = []

# Read and merge all Excel files
for file in excel_files:
    file_path = os.path.join(directory_path, file)
    df = pd.read_excel(file_path)
    dfs.append(df)

# Merge all DataFrames
merged = pd.concat(dfs, ignore_index=True)

# Write the merged data to a new Excel file
merged.to_excel('Matched_Female_Names.xlsx', index=False)

