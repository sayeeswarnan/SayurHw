# Get two names from the user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate the lengths of the two names
len1 = len(name1)
len2 = len(name2)

# Check if the lengths are not equal
if len1 < len2:
    # Add 'a' to the end of name1 until its length is equal to len2
    while len(name1) < len2:
        name1 += 'a'
elif len1 > len2:
    # Add 'a' to the end of name2 until its length is equal to len1
    while len(name2) < len1:
        name2 += 'a'

# Print the modified names
print("Modified names:")
print(name1)
print(name2)
