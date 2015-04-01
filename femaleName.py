#Imports
import json 
#from pprint import pprint Not used
from random import randint

#The best name is a simple name
print ("Only female names Generator")

#def option = null

with open('dataFemale.json') as data_file:    
    data = json.load(data_file)

#Only to show how many combinations can be possible 
print("Until now...")
s = str(len(data.get("names"))) + " Differents names..."
print(s)
s = str(len(data.get("lastnames"))) + " Differents lastnames..."
print(s)

#Randomize a name

lenght = len(data["names"]) -1# To better understand, this line will be out from the randint.
random =randint(0,lenght)
randomName =  data["names"][random]

lenght = len(data["lastnames"]) -1 # To better understand, this line will be out from the randint.
random =randint(0,lenght)
randomLast =  data["lastnames"][random]

s = randomName +" " +randomLast
print(s)