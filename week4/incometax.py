''' find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary.'''


name = input("Enter your name:")
income = int(input("Enter your monthly income from all sources:"))
deduction = 100000
income_gross = income - deduction

if income_gross > 250000:
    print("Do you need old regime or new regime!")
    choice = int(input("Enter 1 for old regime and 2 for new regime:"))

    if choice == 1:
        slab_diffs = [250000, 500000, 1000000]
        tax_percentage = [0.05, 0.1, 0.2]
    elif choice == 2:
        slab_diffs = [300000, 600000, 900000, 1200000, 1500000]
        tax_percentage = [0.05, 0.1, 0.15, 0.2, 0.3]
    else:
        print("Invalid option")
        exit()

    cess_rate = 0.04
    tax = 0

    for i in range(len(slab_diffs)):
        if income_gross >= slab_diffs[i]:
            remaining_amount = income_gross - slab_diffs[i]
            if i == 0:
                tax += (slab_diffs[i] * tax_percentage[i])
            else:
                tax += (remaining_amount * tax_percentage[i])
            cess = tax * cess_rate
            tax += cess

    if tax != 0:
        print("Your 4% cess amount is Rs.", cess)
        print("Tax payable amount is Rs.", tax)
    else:
        print("No need to pay tax after deduction")

else:
    print("No need to pay tax after deduction")


    ''' find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary.'''


# name=input("Enter your name:")
# #Input from  user per month income
# income=int(input("Enter u are monthly income in all source of income :"))

# # all type of deuction (Land,HRA,Insurence,etc..,)
# deduction=100000
# incomegross=income-deduction
# if(incomegross>250000):
#     # to find reduce amount from income
#     print("Do u need oldregime or newregime!")
#     choice=int(input("Enter 1 for oldregime and 2 for newregime:"))
#     if(choice==1):
#         #difference amount slab 2.5 lk 
#         slabdiffs=[250000,500000,1000000] 
#         #difference amount 5 Lk
#         #after decution amount greater than 10 lahks then 30%
#         if incomegross >= slabdiffs[2]:
#          # to sperate each amount to each slab and find final amount in the required slab
    
#             remaining_amount=incomegross-slabdiffs[2]  #It give the required amount from the needed slab
#             #Tax amount calculation 
#             tax=112500+(0.3*(remaining_amount))
#             #For the 4% cess tax for education etc,
#             cess=(0.04*(tax))
#             #after the cess added amount
#             tax=tax+cess 
    

#         #after decution amount greater than 5 lahks then 20%
#         if slabdiffs[1] >= incomegross < slabdiffs[2]:

#             #It give the required amount from the needed slab
#             remaining_amount=incomegross-slabdiffs[1]
#             #Tax amount calculation
#             tax=12500+(0.2*(remaining_amount))
#             #For the 4% cess tax for education etc,
#             cess=(0.04(tax))
#             #after the cess added amount
#             tax=tax+cess
    

#         #after decution amount greater than 2.5 lakhs  then 5%
#         if incomegross >= slabdiffs[0]:
#             remaining_amount=incomegross-slabdiffs[0]
#             tax=(0.05*(remaining_amount))
#             cess=(0.04*(tax))
#             # after the cess added in amount
#             tax=tax+cess
    
#         # if after deduction less than 2.5lakhs no tax
#         if incomegross < slabdiffs[0]:
#             cess=0
#             tax=0 
#         if(tax!=0):
#             print("Your 4% cess amount is Rs.",cess)
#             print("Tax pay amount is Rs.",tax)
#         else:
#             print("No need to pay tax after deduction")
#     elif(choice==2):
#         newslabdiff=[300000,600000,900000,1200000,1500000]
    
#         if incomegross >= newslabdiff[4]:
#             # to sperate each amount to each slab and find final amount in the required slab
    
#             remaining_amount=incomegross-newslabdiff[4]   #It give the required amount from the needed slab
#             #Tax amount calculation 
#             tax=150000+(remaining_amount*30)/100
#             #For the 4% cess tax for education etc,
#             cess=(0.04*(tax))
#             #after the cess added amount
#             tax=tax+cess 
    
#         if newslabdiff[3]>= incomegross <newslabdiff[4]:
#             # to sperate each amount to each slab and find final amount in the required slab
    
#             remaining_amount=incomegross-newslabdiff[3]
#             #Tax amount calculation 
#             tax=90000+(0.20*(remaining_amount))
#             #For the 4% cess tax for education etc,
#             cess=(tax*4)/100
#             #after the cess added amount
#             tax=tax+cess

#          #after decution amount greater than 5 lahks then 20%
#         if newslabdiff[2] >= incomegross < newslabdiff[3]:
#             remaining_amount=incomegross-newslabdiff[2]
#             #Tax amount calculation
#             tax=45000+(0.15*(remaining_amount))
#             #For the 4% cess tax for education etc,
#             cess=(tax*4)/100
#             #after the cess added amount
#             tax=tax+cess
    

#          #after decution amount greater than 2.5 lakhs  then 5%
#         if newslabdiff[1] >= incomegross < newslabdiff[2]:
#             remaining_amount=incomegross-newslabdiff[1]
#             tax=15000+(0.10*(remaining_amount))
#             cess=(tax*4)/100
#             # after the cess added in amountsdf
#             tax=tax+cess
    
#         if newslabdiff[0] >= incomegross < newslabdiff[1]:
#             remaining_amount=incomegross-newslabdiff[0]
#             tax=(remaining_amount)*0.05
#             cess=(tax*4)/100
#             # after the cess added in amount
#             tax=tax+cess
#         # if after deduction less than 3lakhs no tax
#         if 0>incomegross < newslabdiff[0]:
#             cess=0
#             tax=0 
        
#         if(tax!=0):    
#             print("Your 4% cess amount is Rs.",cess)
#             print("Tax pay amount is Rs.",tax)
#         else:
#             print("Invalid option")

# else:  #expection cases
#     print("No need to pay tax")
