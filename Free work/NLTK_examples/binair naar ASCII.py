# # De conversie van ASCII naar binair en binair naar ASCII wordt uitgevoerd door de ingebouwde binascii-module.
#  Het heeft een zeer eenvoudig gebruik met functies die de invoergegevens verzamelen en de conversie uitvoeren.
# Het onderstaande programma toont het gebruik van de binascii-module en de functies ervan genaamd b2a_uu en a2b_uu . De uu staat voor "UNIX-to-UNIX-codering",
#  die zorgt voor de dataconversie van strings naar binaire en ascii-waarden zoals vereist door het programma.

import binascii

text = "Simply Easy Learning"

# Encoding text as bytes
text_bytes = text.encode('utf-8')

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text_bytes)
print ("**Binary to Ascii** \n")
print (data_b2a)

# Converting back from ascii to binary 
data_a2b = binascii.a2b_uu(data_b2a)
print ("**Ascii to Binary** \n")
print (data_a2b.decode('utf-8'))
