######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.

# initializing the range of multiplication tables
start_number = 7
endvalue = 16

# initializing the number of rows
num_rows = 12

# Loop through each number in the range
for num in range(start_number, endvalue + 1):
    print(f"Multiplication Table for {num}:")
    
    # Loop through each row
    for i in range(1, num_rows + 1):
        # Calculating the product
        mul = num * i
        
        # Printing the row
        print(f"{num} x {i} = {mul}")
    
    # Adding a separator between tables
    print("-------------------------")