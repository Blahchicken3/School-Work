#!/usr/bin/env python3

#Set the variables initial values
PayRate = float(input("Enter pay rate "))
Hours = float(input("Enter amount of hours worked "))

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


