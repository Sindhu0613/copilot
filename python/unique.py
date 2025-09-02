import pandas as pd

# Load the Excel file into a DataFrame
source_file = r'C:\\Users\\Admin\\Documents\\huzurabad data\\filtered_data_fb.xlsx'
df = pd.read_excel(source_file)

# Get rows with unique Telugu Names
unique_telugu_names = df.drop_duplicates(subset=['Telugu Names'], keep=False)

# Get rows with duplicate Telugu Names
duplicate_telugu_names = df[df.duplicated(subset=['Telugu Names'], keep=False)]

# Saving unique Telugu Names and their rows to a new Excel file
unique_telugu_names.to_excel(r'C:\\Users\\Admin\\Documents\\python\\unique_telugu_names.xlsx', index=False)

# Saving duplicate Telugu Names and their rows to a new Excel file
duplicate_telugu_names.to_excel(r'C:\\Users\\Admin\\Documents\\python\\duplicate_telugu_names.xlsx', index=False)
