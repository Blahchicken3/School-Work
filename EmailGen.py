#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

#Welcome message
print('Hello! This program will generate emails given first and last names')
print('')

#Set initial values
First = []
Last = []
EmailList = []
More = 'Yes'

#Loop that asks for user input of names
while More in ['Yes', 'yes', 'YES']:
    #Ask user for first name
    First = input('Enter first name: ')
    print('\033[A                                                   \033[A')
    #Ask user for last name
    Last = input('Enter last name: ')
    print('\033[A                                                   \033[A')
    #Creates email with given name
    Email = First+'.'+Last+'@ivytech.edu'
    #Adds email generated above to a list
    EmailList.append(Email)
    #Asks user if there are any more names to enter
    More = input('Do you have any more names to enter? (Yes or No): ')
    print('\033[A                                                               \033[A')
    #Loop to make sure input is valid
    while More not in ['Yes', 'yes', 'YES', 'No', 'no', 'NO']:
        #Outputs a message saying the input isn't valid
        print("Sorry, didn't understand that. Try again.")
        #Asks user if there are any more names to enter
        More = input('Do you have any more names to enter? (Yes or No): ')
        print('\033[A                                                   \033[A')
        print('\033[A                                                   \033[A')
#Exit loop
if More in ['No', 'no', 'NO']:
    #Outputs a message that the list of emails are as followed
    print('Here is the list of emails generated: ')
    #Added a space to make it look cleaner
    print('')
    #Outputs list of emails
    print(EmailList)
    #Added a space to make it look cleaner
    print('')