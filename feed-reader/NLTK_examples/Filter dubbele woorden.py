# Vaak moeten we de tekst alleen analyseren op de unieke woorden die in het bestand aanwezig zijn. We moeten dus de dubbele woorden uit de tekst verwijderen.
# Dit wordt bereikt door het gebruik van het woord tokenisatie en set-functies die beschikbaar zijn in nltk.

# In het onderstaande voorbeeld tokeniseren we de zin eerst in woorden. Vervolgens passen we de functie set() toe, die een ongeordende verzameling unieke elementen creëert.
# Het resultaat bevat unieke woorden die niet geordend zijn.

import nltk
word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour." 

# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)

# Applying Set
no_order = list(set(nltk_tokens))

print (no_order)


# Het behoud van de Orde
# Om de woorden te krijgen nadat we de duplicaten hebben verwijderd, maar toch de volgorde van de woorden in de zin behouden,
# lezen we de woorden en voegen we deze toe aan de lijst door ze toe te voegen.

import nltk
word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour." 
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)

ordered_tokens = set()
result = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
     
print (result)
