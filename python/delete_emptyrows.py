import pandas as pd

# Load the Excel file into a DataFrame
file_path = r'C:\\Users\\Admin\\Documents\\documents\\srinivas\\Sheep Distributing_srinivas Goud_new.xlsx'
column_name = 'MOBILE_NO'  # Replace 'Column_Name' with the name of your column

# Read the Excel file
df = pd.read_excel(file_path)

# Drop rows with empty values in the specified column
df_cleaned = df.dropna(subset=[column_name])

# Save the cleaned data to a new Excel file
output_file_path = r'C:\\Users\\Admin\\Documents\\documents\\srinivas\\Sheep Distributing_srinivas Goud_final.xlsx.xlsx'
df_cleaned.to_excel(output_file_path, index=False)
