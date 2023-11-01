import pprint

student_dict = {'Name': 'Tusar', 'Class': 'XII', 
     'Address': {'FLAT ':1308, 'BLOCK ':'A', 'LANE ':2, 'CITY ': 'HYD'}}

print (student_dict)
print ("\n")
print ("***With Pretty Print***")
print ("-----------------------")
pprint.pprint(student_dict,width=-1)

# JSON-gegevens verwerken
# Pprint kan ook JSON-gegevens verwerken door ze in een beter leesbaar formaat te formatteren.

import pprint

emp = {"Name":["Rick","Dan","Michelle","Ryan","Gary","Nina","Simon","Guru" ],
   "Salary":["623.3","515.2","611","729","843.25","578","632.8","722.5" ],   
   "StartDate":[ "1/1/2012","9/23/2013","11/15/2014","5/11/2014","3/27/2015","5/21/2013",
      "7/30/2013","6/17/2014"],
   "Dept":[ "IT","Operations","IT","HR","Finance","IT","Operations","Finance"] }

x= pprint.pformat(emp, indent=2)
print (x)