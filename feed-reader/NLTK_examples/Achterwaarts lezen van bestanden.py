# Wanneer we normaal gesproken een bestand lezen, wordt de inhoud regel voor regel gelezen vanaf het begin van het bestand.
# Maar er kunnen scenario's zijn waarin we eerst de laatste regel willen lezen.
#  De gegevens in het bestand hebben bijvoorbeeld de nieuwste record onderaan en we willen eerst de nieuwste records lezen. Om aan deze vereiste te voldoen,
# installeren we het vereiste pakket om deze actie uit te voeren met behulp van de onderstaande opdracht.

# pip install file-read-backwards 

with open ("Path\GodFather.txt", "r") as BigFile:
    data=BigFile.readlines()

# Print each line
for i in range(len(data)):
    print( "Line No- "),i 
    print (data[i])


# Wanneer we het bovenstaande programma uitvoeren, krijgen we de volgende uitvoer −

# Line No-  0
# Vito Corleone is the aging don (head) of the Corleone Mafia Family. 

# Line No-  1
# His youngest son Michael has returned from WWII just in time to see the wedding of Connie Corleone (Michael's sister) to Carlo Rizzi. 

# Line No-  2
# All of Michael's family is involved with the Mafia, but Michael just wants to live a normal life. Drug dealer Virgil Sollozzo is looking for Mafia families to offer him protection in exchange for a profit of the drug money. 

# Line No-  3
# He approaches Don Corleone about it, but, much against the advice of the Don's lawyer Tom Hagen, the Don is morally against the use of drugs, and turns down the offer.

# Line No-  4
# This does not please Sollozzo, who has the Don shot down by some of his hit men. 

# Line No-  5
# The Don barely survives, which leads his son Michael to begin a violent mob war against Sollozzo and tears the Corleo