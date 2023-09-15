'''
########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
inputString = #FillinMissingCode
i = 0 #counter to track the chars
newString = ""
while i < len(inputString):
    newString += #FillinMissingCode (assign the from i, i+1 of inputString)
    newString += " " #add space
    i+=2
#check to add the chars at the end
#FillinMissingCode

print (newString)
'''

# Get an input string from the user
inputString = input("Enter a string: ")

i = 0  # Counter to track the characters
newString = ""

while i < len(inputString):
    newString += inputString[i:i + 2]  # Add characters from i to i+2 (exclusive) to newString
    newString += " "  # Add a space
    i += 2  # Move to the next pair of characters

# Check to add the remaining characters at the end
if i < len(inputString):
    newString += inputString[i:]

print(newString)

"""
Output:
Enter a string: Rabbit
Ra bb it
"""
