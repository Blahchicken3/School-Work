#!/usr/bin/env python3

#Set variables initial values
NumList = []
Num = int(1)

#Loop until user enters "0"
while Num != int(0):
    #Ask the user to enter a number
    Num = float(input('Enter a number (Type 0 to exit): '))
    print('\033[A                                                   \033[A')
    #Checks if the number has anything after the decimal
    if int(Num) == Num:
        #If nothing past decimal, converts float to int
        Num = int(Num)
    #Adds input to the list of numbers
    NumList.append(Num)
    #Checks if the number is not equal to 0, and displays it if it does not equal 0
    if Num != 0:
        print(Num)
    
else:
    #If 0 is on the list then this removes it
    NumList.remove(0)
    #Displays the largest number in the list
    print('The largest number in the list is: ', max(NumList))
