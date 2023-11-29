# Vaak moeten we de inhoud van een bestand sorteren voor analyse. We willen bijvoorbeeld dat de zinnen die door verschillende leerlingen zijn geschreven,
# in alfabetische volgorde van hun naam worden gerangschikt. Dat betekent dat u niet alleen sorteert op het eerste teken van de regel,
# maar ook op alle tekens vanaf de linkerkant. In het onderstaande programma
# lezen we eerst de regels uit een bestand en printen ze vervolgens met behulp van de sorteerfunctie die deel uitmaakt van de standaard Python-bibliotheek.

FileName = ("path\poem.txt")
data=file(FileName).readlines()
for i in range(len(data)):
   print (data[i])

