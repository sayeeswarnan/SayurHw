############## Problem  3  #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5, 23, 21, 14, 23, 12, 4, 12, 22, 22, 34, 12]
baseSalary = 10000
bonusFor5Phones = 5000
bonusPerPhoneAfter5 = 1100
additionalBonus = 5000

previousMonthSalary = 0

for month, phoneCount in enumerate(monthlySalesList):
    # Calculate the Salary using if statements

    # Base salary
    currentMonthSalary = baseSalary

    # Bonus for 5 phones sold
    if phoneCount >= 5:
        currentMonthSalary += bonusFor5Phones

    # Bonus for each additional phone after the first 5
    if phoneCount > 5:
        currentMonthSalary += (phoneCount - 5) * bonusPerPhoneAfter5

    # Check for additional bonus condition
    if previousMonthSalary > 20000 and phoneCount >= 20:
        currentMonthSalary += additionalBonus

    print(f"This month's salary before additional bonus: {currentMonthSalary}")

    previousMonthSalary = currentMonthSalary