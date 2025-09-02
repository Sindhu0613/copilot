import pandas as pd

# Load the two Excel sheets into Pandas dataframes
excel1 = pd.read_excel('C:\\Users\\Admin\\Documents\\telangana\\matching data\\Names.xlsx')
excel2 = pd.read_excel('C:\\Users\\Admin\\Documents\\telangana\\matching data\\SIDDIPET_ShadhiMubarak_kalyanalaksmi_uniques.xlsx')

# Assuming the column names containing names are 'Names' in both sheets
column_name = 'Telugu_Names'

# Find matching names between the two sheets
matching_names = excel1[excel1[column_name].isin(excel2[column_name])]

# Save the matching names to a new Excel file
matching_names.to_excel('SP_SM_KL.xlsx', index=False)
