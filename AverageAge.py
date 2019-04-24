#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

#Set variables initial values
AgeList = []
Age = int(1)
Count = 0

#Welcome message
print('Hello! This program will give you the average of any amount of ages you enter.')
#Loop until user enters "0"
while Age != int(0):
    #Ask the user to enter a number
    Age = int(input('Enter an age (Type 0 to exit): '))
    print('\033[A                                                                                   \033[A')
    Count = Count+1
    #Add age to age list
    AgeList.append(Age)
    #Checks if the number is not equal to 0, and displays it if it does not equal 0
    if Age > int(0):
        print('\033[A                                                                               \033[A')
        print(AgeList)
    #If the age entered is less than 0, if will remove it from the list, and remove 1 from the variable "Count"
    elif Age < int(0):
        AgeList.remove(Age)
        Count = Count-1
    #If the age entered is less than 0, Tell the user it is an invalid age, and to try again
    while Age < int(0):
        print('\033[A                                                                               \033[A')    
        print("You can't have a negative age, try again")
        Age = int(input('Enter an age (Type 0 to exit): '))
        print('\033[A                                                                               \033[A')             
        #Once a valid age is entered, continue with the program until 0 is entered
        if Age > int(0):
            Count = Count+1
            #Add age to age list
            AgeList.append(Age)
            print('\033[A                                                                           \033[A')
            print(AgeList)
else:
    #If 0 is in the list then this removes it
    AgeList.remove(0)
    Count = Count-1
    Average = int(sum(AgeList)/Count)
#Displays the largest number in the list
print("The average age is:",Average)