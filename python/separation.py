import pandas as pd

# Sample DataFrame
file_path = r'C:\\Users\\Admin\\Documents\\huzurabad data\\output_file.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Filter rows where 'MOBILE_NO' column contains mobile numbers
mobile_number_pattern = r'\d{10}'  # Assuming mobile numbers are 10 digits
filtered_df = df[df['MOBILE_NO'].str.contains(mobile_number_pattern, na=False)]

output_file_path = 'phn number.xlsx'  # Replace with your desired output file path
filtered_df.to_excel(output_file_path, index=False)  # Save the filtered DataFrame
