#!/usr/bin/env python3

import random

#Set variables initial values
Card = range(1,52)
Clubs = range(1,13)
Diamonds = range(14,26)
Hearts = range(27,39)
Spades = range(40,52)
Cl = []
Di = []
He = []
Sp = []
Count = 1
Num = int(0)

#Loop until 1000 numbers have been generated
while Count < 1001:
    #Randomly select number from 1-52
    Num = random.choice(Card)
    #Depending on the number generated, add it to the correct list
    if Num in Clubs:
        Cl.append(1)
        Count = Count+1
    elif Num in Diamonds:
        Di.append(1)
        Count = Count+1
    elif Num in Hearts:
        He.append(1)
        Count = Count+1
    elif Num in Spades:
        Sp.append(1)
        Count = Count+1

#Output the totals for each suit
print('There are',Cl.count(1),'Clubs')
print('There are',Di.count(1),'Diamonds')
print('There are',He.count(1),'Hearts')
print('There are',Sp.count(1),'Spades')