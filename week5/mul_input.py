'''
7.Challange questions
Ask the user which tables he/she wants to print (eg 2,9,7,12)
Also ask if they want to see the basic only or advanced only or both.
Hint - use list to get the user input and learn how to use a list in range statement
'''
print("My Tables")

table_numbers = input("Enter the number tables you want to print (comma-separated, e.g., 1,2,3): ").split(',')#.The input is split into individual numbers using .split(',')

table_numbers = [int(num) for num in table_numbers]# list of numbers is converted to integers and stored in the table_numbers variable.

choice = input("Do you want to print 'Basic', 'Advanced', or 'Both'? (Type 'Quit' to exit): ").lower()#The input is converted lowercase using .lower() 
def print_multiplication_table(table, choice):
    print(f"Table  {table}")

    if 'basic' in choice or 'both' in choice:
        print("Easy numbers")
        for i in range(1, 11):
            result = i * table
            print(f"{i} * {table} = {result}")

    if 'advanced' in choice or 'both' in choice:
        print("Advanced numbers")
        for i in range(11, 21):
            result = i * table
            print(f"{i} * {table} = {result}")

    print("**********")
    print("\n")

for table in table_numbers:
    print_multiplication_table(table, choice)#For each table number, it calls the print_multiplication_table function to print the tables based on the user's choice.
#eg:print_multiplication_table(5, "basic"),It is how it works

print("the end")

