import os
import pandas as pd
# Specify the input folder containing Excel files
input_folder = r'C:\\Users\\Admin\\Documents\\UNIQUES_NAMES_ALL_CONS'
# Specify the output folder for cleaned files
output_folder = r'C:\\Users\\Admin\\Documents\\UNIQUE_NAES_ALL_CLEANED'
# List all Excel files in the input folder
input_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]
# Iterate through each Excel file
for input_file in input_files:
    # Construct full paths for input and output files
    input_path = os.path.join(input_folder, input_file)
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_path)
    # Remove leading and trailing spaces from all columns in the DataFrame
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    # Remove duplicates based on 'Matching_Word' and 'Matching_Telugu_Word'
    df_unique = df.drop_duplicates(subset=['Unique_names', 'Telugu_Unique_names'])
    # Save the unique DataFrame to a new Excel file in the output folder
    output_path = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_unique.xlsx")
    df_unique.to_excel(output_path, index=False)
    print(f'Unique values saved to {output_path}')