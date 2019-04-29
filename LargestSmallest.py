#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

#Set variables initial values
NumList = []
Num = int(1)

#Welcome message
print('Hello! This program will tell you the largest positive number that you enter.')
print('')
#Loop until user enters "0"
while Num != int(0):
    #Ask the user to enter a number
    Num = float(input('Enter a positive number (Type 0 to exit): '))
    print('\033[A                                                           \033[A')
    #Checks if the number has anything after the decimal
    if int(Num) == Num:
        #If nothing past decimal, converts float to int
        Num = int(Num)
    #Checks if the number is not equal to 0, and displays it if it does not equal 0
    if Num > 0:
        #Adds input to the list of numbers
        NumList.append(Num)
        print('\033[A                                                                               \033[A')
        print(Num)
    
else:
    #Displays the largest number in the list
    print(NumList)
    print('')
    print('The largest number in the list is: ', max(NumList))
    print('The smallest number in the list is: ', min(NumList))
