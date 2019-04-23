#!/usr/bin/env python3

#Set the variables initial values
Count = int(1)
Activity = str('')

#Welcome message
print("Hello! I'm going to ask you to input 3 of your favorite activities")
print('These are 3 things you like to do in your free time:')
#Loop until the user has entered 3 activities    
while Count < 4:
    #Ask the user for an activity
    Activity = input('Input activity: ')
    print("\033[A                             \033[A")
    #Output the activity the user enters
    print(Count,'. You enjoy: ',Activity)
    Count = Count + 1
