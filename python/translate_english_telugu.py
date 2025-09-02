import pandas as pd
from deep_translator import GoogleTranslator

# Load your Excel file
file_path = r'C:\\Users\\SriramineniSindu\\Documents\\full name sorted schems\\HH data guntur_Housesites_fn_completed.xlsx'
df = pd.read_excel(file_path)

# Assuming the English names are in a column named 'EnglishNames'
column_name = 'CITIZEN_NAME'

# Translate each name in the column from English to Telugu
translated_names = []
for name in df[column_name]:
    # Split the name into smaller chunks (5000 characters each) for translation
    chunks = [name[i:i+5000] for i in range(0, len(name), 5000)]
    translated_chunks = []
    for chunk in chunks:
        translated_chunk = GoogleTranslator(source='en', target='te').translate(chunk)
        translated_chunks.append(translated_chunk)
    translated_name = ''.join(translated_chunks)
    translated_names.append(translated_name)

# Add the translated names to a new column in the DataFrame
df['CITIZEN_NAME'] = translated_names

# Save the updated DataFrame to a new Excel file
output_file_path = 'translated_names.xlsx'
df.to_excel(output_file_path, index=False)
