import pandas as pd
import regex as re  # Import the 'regex' library for Unicode support

# Define Telugu characters using Unicode range
telugu_characters_pattern = r'[\u0C00-\u0C7F]'

# Read the Excel file
excel_file = r'C:\\Users\\Admin\\Documents\\UNIQUE_NAES_ALL_CLEANED\\UNIQUES_NAMES_ALL_CONS_cln.xlsx'
df = pd.read_excel(excel_file)

# Function to check if a name contains Telugu characters
def contains_telugu(name):
    return bool(re.search(telugu_characters_pattern, name))

# Separate rows based on Telugu characters in names
telugu_names_rows = df[df['Telugu_Unique_names'].astype(str).apply(contains_telugu)]
non_telugu_names_rows = df[~df['Telugu_Unique_names'].astype(str).apply(contains_telugu)]

# Write to separate Excel files
telugu_names_rows.to_excel('telugu_names.xlsx', index=False)
non_telugu_names_rows.to_excel('non_telugu_names.xlsx', index=False)
