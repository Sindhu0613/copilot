import pandas as pd

# Read the source Excel file
source_file = r'C:\\Users\\Admin\\Documents\\31-Huzurabad.xlsx'
df_source = pd.read_excel(source_file)

selected_columns = ['FM_NAME_EN', 'LASTNAME_EN', 'FM_NAME_V1', 'LASTNAME_V1', 'MOBILE_NO']
df_selected = df_source[selected_columns]

# Write the selected columns to a new Excel file
destination_file = 'data.xlsx'
df_selected.to_excel(destination_file, index=False)
print(destination_file)