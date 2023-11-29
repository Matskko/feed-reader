# Synoniemen en Antoniemen zijn beschikbaar als onderdeel van het wordnet, een lexicale database voor de Engelse taal.
# Het is beschikbaar als onderdeel van nltk corpora-toegang. In wordnet zijn synoniemen de woorden die hetzelfde concept aanduiden en in veel contexten uitwisselbaar zijn,
# zodat ze gegroepeerd worden in ongeordende sets (synsets).
# We gebruiken deze synsets om de synoniemen en antoniemen af ​​te leiden zoals weergegeven in de onderstaande programma's.

from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets("Soil"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
print (set(synonyms))
