#!/usr/bin/env python3

Count = int(1)
Activity = str('')

print("Hello! I'm going to ask you to input 3 of your favorite activities")
print('These are 3 things you like to do in your free time:')
    
while Count < 4:
    Activity = input('Input activity: ')
    print("\033[A                             \033[A")
    print(Count,'. You enjoy: ',Activity)
    Count = Count + 1
