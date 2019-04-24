#!/usr/bin/env python3

print('***************************************************')
print('YOU NEED TO USE PYTHON 3 FOR THIS TO WORK PROPERLY')
print('***************************************************')

#Set the variables initial values
PayRate = float(input("Enter pay rate "))
Hours = float(input("Enter amount of hours worked "))

#Welcome message
print('Hello! This program will tell you the total pay depending on how many hours you worked, as well as how much you make per hour')
#Calculate payrate depending on user input of hours worked and hourly wages
if PayRate < 10 or Hours > 40:
    OvertimeHours = (Hours - 40)
    OvertimePay = (OvertimeHours * 1.5 * PayRate)
    TotalPay = (40 * PayRate + OvertimePay)
    #Output the total pay
    print ("Total pay is "+str(round(TotalPay,2)))
else:
    TotalPay = (Hours * PayRate)
    #Output the total pay
    print ("Total pay is "+str(round(TotalPay,2)))


