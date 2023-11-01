# Stopwoorden zijn Engelse woorden die niet veel betekenis aan een zin toevoegen. Ze kunnen veilig worden genegeerd zonder de betekenis van de zin op te offeren.
# Bijvoorbeeld de woorden als de, hij, hebben enz.
# Dergelijke woorden zijn al vastgelegd in het corpus met de naam corpus.
# We downloaden het eerst naar onze Python-omgeving.


# nltk.download('stopwords')

# Er wordt een bestand met Engelse stopwoorden gedownload.

from nltk.corpus import stopwords
stopwords.words('english')
print (stopwords.words() [620:680])


# De verschillende andere talen dan Engels waarin deze stopwoorden voorkomen, zijn zoals hieronder.

from nltk.corpus import stopwords
print (stopwords.fileids())


# We gebruiken het onderstaande voorbeeld om te laten zien hoe de stopwoorden uit de woordenlijst worden verwijderd.

from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

all_words = ['There', 'is', 'a', 'tree','near','the','river']
for word in all_words: 
    if word not in en_stops:
        print(word)
        