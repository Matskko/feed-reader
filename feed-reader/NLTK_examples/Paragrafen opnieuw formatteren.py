# *Het opmaken van alinea's is nodig als we met een grote hoeveelheid tekst omgaan en deze in een presentabel formaat brengen.
# *Mogelijk willen we elke regel met een specifieke breedte afdrukken of proberen we de inspringing voor elke volgende regel te vergroten wanneer we een gedicht afdrukken.
#  *In dit hoofdstuk gebruiken we een module met de naam textwrap3 om de alinea's naar wens op te maken.

# ! Eerst moeten we het vereiste pakket als volgt installeren
# ! pip install textwrap3

from textwrap3 import wrap

text = 'In late summer 1945, guests are gathered for the wedding reception of Don Vito Corleones daughter Connie (Talia Shire) and Carlo Rizzi (Gianni Russo). Vito (Marlon Brando), the head of the Corleone Mafia family, is known to friends and associates as Godfather. He and Tom Hagen (Robert Duvall), the Corleone family lawyer, are hearing requests for favors because, according to Italian tradition, no Sicilian can refuse a request on his daughters wedding day.'

x = wrap(text, 30)
for i in range(len(x)):
    print(x[i])