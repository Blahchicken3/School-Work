#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

#Set variables initial values
NumList1 = []
NumList2 = []
Num = int(1)

#Welcome message
print('Hello! This program will give you the sum of all numbers you enter.')
#Loop until user enters "0"
while Num != int(0):
    #Ask the user to enter a number
    Num = float(input('Enter a number (Type 0 to exit): '))
    print('\033[A                                                       \033[A')
    #Checks if the number has anything after the decimal
    if int(Num) == Num:
        #If nothing past decimal, converts float to int
        Num = int(Num)
    #If input number is positive add it to list one
    if Num > 0:
        NumList1.append(Num)
    #If input number is negative add it to list two
    elif Num < 0:
        NumList2.append(Num)
    #Checks if the number is not equal to 0, and displays it if it does not equal 0
    if Num != 0:
        print(Num)
    
else:
    #If 0 is in either list then this removes it
    if 0 in NumList1:
        NumList1.remove(0)
    if 0 in NumList2:
        NumList2.remove(0)
    #Displays the sums of the numbers in the list
    print('The sum of the positive numbers in the list is: ', sum(NumList1))
    print('The sum of the negative numbers in the list is: ', sum(NumList2))
    print('The sum of the all numbers in the list is: ', sum(NumList2)+sum(NumList1))