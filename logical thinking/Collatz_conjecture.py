# Define a function to calculate the Collatz sequence
def collatz_conjecture(n):
    sequence = [n]  # Initialize a list to store the sequence with the starting number
    while n != 1:  # Continue until n becomes 1
        if n % 2 == 0:  # If n is even
            n = n // 2  # Apply the even rule: divide by 2
        else:
            n = 3 * n + 1  # If n is odd, apply the odd rule: 3n + 1
        sequence.append(n)  # Add the current number to the sequence list
    return sequence  # Return the complete Collatz sequence

# Input from the user
n = int(input("Enter a positive integer: "))  # Prompt the user for input
if n <= 0:
    print("Please enter a positive integer")  # Check if the input is non-positive and provide a message

# Calculate and print the Collatz sequence
result = collatz_conjecture(n)  # Call the collatz_conjecture function to calculate the sequence
print("Collatz Conjecture sequence:", result)  # Print the resulting Collatz sequence
