#!/usr/bin/env python3

PayRate = float(input("Enter pay rate "))
Hours = float(input("Enter amount of hours worked "))

if PayRate < 10 or Hours > 40:
    OvertimeHours = (Hours - 40)
    OvertimePay = (OvertimeHours * 1.5 * PayRate)
    TotalPay = (40 * PayRate + OvertimePay)
    print ("Total pay is "+str(round(TotalPay,2)))
else:
    TotalPay = (Hours * PayRate)
    print ("Total pay is "+str(round(TotalPay,2)))

