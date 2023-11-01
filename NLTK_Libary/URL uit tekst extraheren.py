# URL-extractie wordt bereikt vanuit een tekstbestand met behulp van reguliere expressies.
# De expressie haalt de tekst op waar deze overeenkomt met het patroon. Hiervoor wordt alleen de re-module gebruikt.

# Voorbeeld
# We kunnen een invoerbestand met enkele URL's nemen en dit via het volgende programma verwerken om de URL's te extraheren.
# De functie findall() wordt gebruikt om alle instanties te vinden die overeenkomen met de reguliere expressie.

import re
 
with open("path\url_example.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)
            
            