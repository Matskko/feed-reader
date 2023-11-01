# Tijdens het lezen van een bestand wordt het gelezen als een woordenboek met meerdere elementen.
# We hebben dus toegang tot elke regel van het bestand met behulp van de index van het element.
# In het onderstaande voorbeeld hebben we een bestand met meerdere regels en deze regels worden individuele elementen van het bestand.

with open ("Path\GodFather.txt", "r") as BigFile:
    data=BigFile.readlines()

# Print each line
for i in range(len(data)):
    print ("Line No- "),i 
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
# The Don barely survives, which leads his son Michael to begin a violent mob war against Sollozzo and tears the Corleon