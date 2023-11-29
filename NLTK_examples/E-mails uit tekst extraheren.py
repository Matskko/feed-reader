#  Om e-mails uit tekst te extraheren, kunnen we reguliere expressie gebruiken. In het onderstaande voorbeeld
#  gebruiken we de hulp van het reguliere expressiepakketom het patroon van een e-mail-ID te definiëren en
#  gebruiken we vervolgens de functie findall() om de tekst op te halen die met dit patroon overeenkomt.

import re
text = "Please contact us at contact@tutorialspoint.com for further information."+\
        " You can also give feedbacl at feedback@tp.com"


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)
