#!/usr/bin/env python3

#Set variables initial values
Count = int(1)
Total = int(0)
TotalCash = int(0)
TotalCheck = int(0)
TotalCoin = int(0)
StoreNum = int(1)
MoreStores = str('Yes')

#Welcome message
print("Hello! I'm going to ask you to input all of the checks and cash from each store")

#Check to see if there are more stores being collected from
while MoreStores in ['Yes', 'yes', 'YES']:
    #If the user says there is another store being collected from then it will add 1 to the store number
    StoreNum = StoreNum+1
    #Loop until the count is greater than the amount of stores
    while Count <= StoreNum:
        #Get the amounts from the user
        Check = float(input('Input Check amount: '))
        print('\033[A                                                   \033[A')
        Cash = int(input('Input Cash amount: '))
        print('\033[A                                                   \033[A')
        Coin = int(input('Input Coin amount without decimal: '))
        print('\033[A                                                   \033[A')
        #Output the check and cash amounts for the current store
        print('Store number:',Count,'Check amount: $',(round(Check,2)))
        print('Store number:',Count,'Cash amount: $',round(Cash+(Coin/100),2))
        #Check to see if the amount is positive/valid
        if Check >= int(0) and Cash >= int(0) and Coin >= int(0):
            #Add the current store amounts to the totals
            Count = Count + 1
            TotalCash = float(TotalCash+Cash+(Coin/100))
            TotalCheck = float(TotalCheck+Check)
            Total = float(TotalCheck+TotalCash)
            #Ask the user if there is another store they are collecting from
            MoreStores = input('Do you have another store? Yes or No: ')
            print('\033[A                                                       \033[A')
            #Check that the input from the user is valid, if not then it will ask again
            while MoreStores not in ['Yes', 'yes', 'YES', 'No', 'no', 'NO']:
                MoreStores = input('Do you have another store? Yes or No: ')
                print('\033[A                                                       \033[A')
        #Make suer the user is entering valid amounts collected from the store
        else:
            print("You can't collect negative money from a store! Try again.")   
             
#Output the totals of the checks, cash, and total
print('Total check amount collected: $' + str(round(TotalCheck,2)))
print('Total cash amount collected: $' + str(round(TotalCash,2)))
print('Total amount collected: $' + str(round(Total,2)))
