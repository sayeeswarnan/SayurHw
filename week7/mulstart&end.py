# Get user input for the start and end numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Calculate the number of rows and columns

num_columns = end - start + 2

# Print the header row
print("    ", end="")
for i in range(start, end + 1):
    print(f"{i:3}", end=" ")
print("\n  " + "*" * (num_columns * 4))

# Print the multiplication table
for i in range(start, end + 1):
    print(f"{i:2} |", end=" ")
    for j in range(start, end + 1):
        result = i * j
        print(f"{result:3}", end=" ")
    print()

