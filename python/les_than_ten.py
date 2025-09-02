import pandas as pd


df = pd.read_excel(r'C:\\Users\\SriramineniSindu\\Documents\\data\\new2\\Guntur_West_unique2_completed.xlsx')


df['Mobile'] = df['Mobile'].astype(str)

# Filter rows based on conditions
condition1 = df['Mobile'].str.len() > 10  
condition2 = df['Mobile'].str.len() < 10  
condition3 = df['Mobile'].str.startswith(('0', '1', '2', '3', '4', '5'))  

filtered_rows = df[condition1 | condition2 | condition3]
remaining_rows = df[~(condition1 | condition2 | condition3)]  

with pd.ExcelWriter('filtered_data.xlsx') as writer:
    filtered_rows.to_excel(writer, sheet_name='Filtered Data', index=False)
    remaining_rows.to_excel(writer, sheet_name='Remaining Data', index=False)
