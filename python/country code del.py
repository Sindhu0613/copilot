import pandas as pd

# Load the Excel file into a pandas DataFrame
file_path = r'C:\\Users\\Admin\\Documents\\srinivas\\Dalitha_Bandhu_SrinivasGoud.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Display the initial few rows to verify the data
print("Before replacing:")
print(df.head())

# Convert 'Mobile Number' column to string type if not already done
df['MOBILE_NO'] = df['MOBILE_NO'].astype(str)

# Remove '+91' from the 'Mobile Number' column and strip any leading or trailing spaces
df['MOBILE_NO'] = df['MOBILE_NO'].str.replace(r'^\+?91', '', regex=True).str.strip()

# Display the modified DataFrame to verify the changes
print("\nAfter replacing +91:")
print(df.head())

# Save the modified DataFrame back to an Excel file if needed
output_file_path = 'output_file.xlsx'  # Replace with your desired output file path
df.to_excel(output_file_path, index=False)
