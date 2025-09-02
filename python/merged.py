import pandas as pd

source_file = r'C:\\Users\\Admin\\Documents\\ibp data\\ibt_data.xlsx'
df = pd.read_excel(source_file)

# Merging columns into a new column 'Names'
df['Names'] = df['FM_NAME_V1'] + ' ' + df['LASTNAME_V1'].fillna('')

# Merging other columns into a new column 'Telugu Names'
#df['Telugu Names'] = df['FM_NAME_V1'] + ' ' + df['LASTNAME_V1'].fillna('')

# Dropping and renaming columns
df.drop(['FM_NAME_V1', 'LASTNAME_V1'], axis=1, inplace=True)

# Saving the modified DataFrame to a new Excel file
df.to_excel(r'C:\\Users\\Admin\\Documents\\python\\ibt.xlsx', index=False)
