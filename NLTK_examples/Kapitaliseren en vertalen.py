# Tekenreeksen met hoofdletters zijn een normale behoefte in elk tekstverwerkingssysteem. Python bereikt dit door gebruik te maken van de ingebouwde functies in de standaardbibliotheek.
# In het onderstaande voorbeeld gebruiken we de twee stringfuncties capwords() en upper() om dit te bereiken.
# Terwijl 'capwords' de eerste letter van elk woord met een hoofdletter schrijft,geeft 'upper' de hele reeks met een hoofdletter.
import string
text = 'Tutorialspoint - simple easy learning.'

# Capitalize the words (title case)
capitalized_text = string.capwords(text)
print(capitalized_text)

# Convert the entire string to uppercase
uppercase_text = text.upper()
print(uppercase_text)


# Trnslatie in Python betekent in wezen het vervangen van specifieke letters door een andere letter. Het kan werken voor het versleutelen van tekenreeksen.


text = 'Tutorialspoint - simple easy learning.'

# Maak een vertalingstabel voor vervangingen
transtable = str.maketrans('tpol', 'wxyz')

# Gebruik de vertalingstabel om de tekst te wijzigen
translated_text = text.translate(transtable)
print(translated_text)
