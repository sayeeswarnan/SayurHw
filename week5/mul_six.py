number = int(input("Enter the table number you want:"))
# Get the choice from the user
choice = str(input("Enter 'basic' for basic table\nEnter 'advance' for advance table\nEnter 'both' for both 'advance' and 'basic' tables: "))
print(f"My Tables {number}")

if 'basic' in choice or 'both' in choice:
    print("Basic numbers")
    for num in range(1, 11):
        print(f"{number} * {num} = {number * num}")
    
    print("***********") 
    print("")

if 'advance' in choice or 'both' in choice:
    print("Advanced numbers")
    for num in range(11, 21):
        print(f"{number} * {num} = {number * num}")
    
    print("************")    
else:
    print("Invalid choice. Please enter your choice properly.")

print("End of table")