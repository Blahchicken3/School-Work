#!/usr/bin/env python3

#Set variables initial values
Count = int(1)
Total = int(0)
TotalCash = int(0)
TotalCheck = int(0)
TotalCoin = int(0)

#Welcome message
print("Hello! I'm going to ask you to input all of the checks and cash from each store")
#Ask user to input the amount of stores they are collecting from
StoreNum = int(input('How many stores are you collecting from?: '))

#Check if store number is valid
if StoreNum > 0:
    #Loop the amount of times of the amount of stores being visited
    while Count <= StoreNum:
        #Ask user for check, cash, and coin amounts, and clear the input field to only show the output, and not the input message
        Check = float(input('Input Check amount: '))
        print('\033[A                                                   \033[A')
        Cash = int(input('Input Cash amount: '))
        print('\033[A                                                   \033[A')
        Coin = int(input('Input Coin amount without decimal: '))
        print('\033[A                                                   \033[A')
        #Output the store number and check and cash amount per store
        print('Store number:',Count,'Check amount: $',(round(Check,2)))
        print('Store number:',Count,'Cash amount: $',round(Cash+(Coin/100),2))
        #Check if the entered values are greater than 0
        if Check >= int(0) and Cash >= int(0) and Coin >= int(0):
            #Add previous store amount to the total amounts
            Count = Count + 1
            TotalCash = float(TotalCash+Cash+(Coin/100))
            TotalCheck = float(TotalCheck+Check)
            Total = float(TotalCheck+TotalCash)
        #If amount is negative, loop back to ask for the amounts again
        else:
            print("You can't collect negative money from a store! Try again.")
#If the amount of stores entered is less than 1 then it will exit the program and tell the user to try again
elif StoreNum <= 0:
    print('Not a valid number of stores, try again.')

#Output the total amounts of check, cash, and everything collected
print('Total check amount collected: $' + str(round(TotalCheck,2)))
print('Total cash amount collected: $' + str(round(TotalCash,2)))
print('Total amount collected: $' + str(round(Total,2)))