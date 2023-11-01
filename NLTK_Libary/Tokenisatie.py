# In Python verwijst tokenisatie in feite naar het opsplitsen van een grotere hoeveelheid tekst in kleinere regels, woorden of zelfs het creëren van woorden voor een niet-Engelse taal.
# De verschillende tokenisatiefuncties zijn ingebouwd in de nltk-module zelf en kunnen worden gebruikt in programma's zoals hieronder weergegeven.

# Lijntokenisatie
# In het onderstaande voorbeeld verdelen we een gegeven tekst in verschillende regels door de functie sent_tokenize te gebruiken.

import nltk
sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)


# Niet-Engelse tokenisatie
# In het onderstaande voorbeeld tokeniseren we de Duitse tekst.


german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('Wie geht es Ihnen?  Gut, danke.')
print(german_tokens)

# Woord Tokenzitaion
# We tokeniseren de woorden met behulp van de functie word_tokenize die beschikbaar is als onderdeel van nltk.

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)
