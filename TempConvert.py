#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

#Welcome message
print('Hello! This program will allow you to enter a temperature in celsius and output the same temperature in fahrenheit.')
print('')

#Set variables to initial values
CTemp = float(0)
FTemp = float(0)

#Loop calculations until user enteres "-999"
while CTemp != -999:
    #Ask the user for input
    CTemp = float(input('Please enter a temp in celsius (Enter "-999" to exit): '))
    #Convert input of C to F
    FTemp = 9*CTemp/5+32
    #Check if they are equal to an integer, and if so convert them from float to integer
    if int(CTemp) == CTemp:
        CTemp = int(CTemp)
    if int(FTemp) == FTemp:
        FTemp = int(FTemp)
    print('\033[A                                                                       \033[A')
    #Prints the temp input and its F equivalent
    print(round(CTemp,2),'C° =',round(FTemp,2),'F°')
    #If user enters "-999" exits the program and doesn't output -999 C to F
    if CTemp == -999:
        print('\033[A                                   \033[A')