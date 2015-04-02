#Imports
import json 
#from pprint import pprint Not used
from random import randint
from random import randDouble
#The best name is a simple name
print ("Male Character")

#def option = null Not used

with open('dataMale.json') as data_file:    
    data = json.load(data_file)

#Only to show how many combinations can be possible 
print("Until now...")
s = str(len(data.get("names"))) + " Differents names..."
print(s)
s = str(len(data.get("lastnames"))) + " Differents lastnames..."
print(s)
print()
print("===Character===")
print()
#Randomize a name

lenght = len(data["names"]) -1# To better understand, this line will be out from the randint.
random =randint(0,lenght)
randomName =  data["names"][random]

lenght = len(data["lastnames"]) -1 # To better understand, this line will be out from the randint.
random =randint(0,lenght)
randomLast =  data["lastnames"][random]

s = randomName +" " +randomLast #NPC name
p = "Peculiars:" #NPC peculiars
randomQPeculiar = randint(1,3) #Random number of peculiars in a NPC
for i in range(randomQPeculiar):
	lenght = len(data["peculiar"]) -1 # To better understand, this line will be out from the randint.
	random =randint(0,lenght)		
	randomPeculiar = data["peculiar"][random] 
	while(randomPeculiar in p):
		random =randint(0,lenght)		
		randomPeculiar = data["peculiar"][random]
	p = p +" " +randomPeculiar

#Weakness

age = randint(5,90)
height = randint() #If not dwarf
weight = randint() #If not dwarf
print(s)
print(p)