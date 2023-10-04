def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Input a positive integer
num = int(input("Enter a positive integer: "))

# Create the Collatz sequence
sequence = collatz_sequence(num)

# Find the largest number in the sequence
largest_number = max(sequence)

print("Collatz sequence:", sequence)
print("Largest number in the sequence:", largest_number)
