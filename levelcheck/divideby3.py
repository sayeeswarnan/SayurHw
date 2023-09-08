# Initialize a count variable to keep track of the number of divisions
count = 0

# Get a number from the user
number = float(input("Enter a number: "))

# Check if the number is initially less than 3
if number < 3:
    print("The number is already less than 3.")
else:
    # Continue dividing by 3 until the number is less than 3
    while number >= 3:
        number /= 3  # Divide the number by 3
        count += 1    # Increment the count

    # Print the final result and the number of divisions
    print(f"The final result is: {number}")
    print(f"The number was divided {count} times.")
