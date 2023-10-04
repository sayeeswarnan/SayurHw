def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Input two positive integers
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))
if num1 <= 0 or num2 <= 0:
    print("Enter the positive integers of two values")

# Calculate the steps needed for each number
steps1 = collatz_steps(num1)
steps2 = collatz_steps(num2)

# Compare and print the result
if steps1 < steps2:
    print(f"{num1} takes fewer steps to reach 1.")
elif steps2 < steps1:
    print(f"{num2} takes fewer steps to reach 1.")
else:
    print(f"{num1} and {num2} take the same number of steps to reach 1.")