#!/usr/bin/env python3

Count = int(1)
Total = int(0)
TotalCash = int(0)
TotalCheck = int(0)
TotalCoin = int(0)

print("Hello! I'm going to ask you to input all of the checks and cash from each store")
StoreNum = int(input('How many stores are you collecting from?: '))

if StoreNum > 0:    
    while Count <= StoreNum:
        Check = float(input('Input Check amount: '))
        print('\033[A                                                   \033[A')
        Cash = int(input('Input Cash amount: '))
        print('\033[A                                                   \033[A')
        Coin = int(input('Input Coin amount without decimal: '))
        print('\033[A                                                   \033[A')
        print('Store number:',Count,'Check amount: $',(round(Check,2)))
        print('Store number:',Count,'Cash amount: $',round(Cash+(Coin/100),2))
        if Check >= int(0) and Cash >= int(0) and Coin >= int(0):
            Count = Count + 1
            TotalCash = float(TotalCash+Cash+(Coin/100))
            TotalCheck = float(TotalCheck+Check)
            Total = float(TotalCheck+TotalCash)
        else:
            print("You can't collect negative money from a store! Try again.")
elif StoreNum <= 0:
    print('Not a valid number of stores, try again.')

print('Total check amount collected: $' + str(round(TotalCheck,2)))
print('Total cash amount collected: $' + str(round(TotalCash,2)))
print('Total amount collected: $' + str(round(Total,2)))
