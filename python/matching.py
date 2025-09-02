import pandas as pd

# Define Telugu independent vowels and consonants
#telugu_independent_vowels = "అఆఇఈఉఊఋఎఏఐఒఓఔ"
#telugu_consonants = "కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళఴవశషసహ"
telugu_various_signs = "\u0C01\u0C02\u0C03"
telugu_dependent_vowel_signs = "\u0C3E\u0C3F\u0C40\u0C41\u0C42\u0C43\u0C44\u0C46\u0C47\u0C48\u0C4A\u0C4B\u0C4C\u0C4D\u0C60\u0C56"
# Read the Excel file
excel_file = r'C:\\Users\\Admin\\Documents\\merge\\Final_UniqueNames.xlsx'  # Replace with your file name
df = pd.read_excel(excel_file)

# Function to check if a name starts with Telugu characters
def starts_with_telugu(name):
    return name[0] in telugu_various_signs or name[0] in telugu_dependent_vowel_signs

# Separate rows based on starting characters of names
telugu_start_rows = df[df['Telugu_Unique_names'].apply(starts_with_telugu)]
non_telugu_start_rows = df[~df['Telugu_Unique_names'].apply(starts_with_telugu)]

# Write to separate Excel files
telugu_start_rows.to_excel('telugu_start_names.xlsx', index=False)
non_telugu_start_rows.to_excel('non_telugu_start_names.xlsx', index=False)
