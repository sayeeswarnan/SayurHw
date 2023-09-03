print("  \tyou can calculate upto 500 units \n Because the program is based on Average units consumed in house")
Units = float(input("Enter The Number of units : "))
rate = [0,2.25,4.5,6]
if Units>=1 and Units<=100:
    rate=rate[0]
    #calculation how the unit bill is generated
    Amount = Units*rate
  
    print( "your bill amount is: " ,str(Amount))
    print("Due to Goverment subsidy plan you have no amount Because \nyour unit is below 100")
elif Units>=101 and Units<=200:
    
    Amount = (100*0) + (Units - 100)*rate[1]
    print( "your bill amount is: " + str(Amount))
elif Units>=201 and Units<=300:
    
    Amount = (100*0) + (200 - 100) * 2.25 +(Units- 200) * rate[2]
    print( "your bill amount is: " + str(Amount))
    
elif Units>=301 and Units<=400:
    
    Amount = (100*0) + (200 - 100) * 2.25 + (300-200) * 4.5 + (Units - 300) * rate[2]
  
    print( "your bill amount is: " + str(Amount))

elif Units>=401 and Units<=500:
    
    Amount = (100*0) + (200 - 100) * 2.25 + (300-200) * 4.5 +(400-300) * 4.5 +(Units -500)*rate[35]

   
    print( "your bill amount is: " + str(Amount))
   

else:
    print("\tyou can calculate upto 500 units \n Because the program is based on Average units consumed in house\n so enter the amount properly")
    '''
    for i in range(1,11):
    print(i,"*")
    for k in range(1,5):
        print(k)
j=8
print(j)
print("\n")
    '''