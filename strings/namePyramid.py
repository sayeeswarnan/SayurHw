# ########## Program 2
# #Print your name in a pyramid
# #eg RAM
# #R
# #RA
# #RAM

# myName = #FillinMissingCode
# for letter in myName:
#     print(#FillinMissingCode)

myName = input("enter the name:") #Enter your name eg:RAM

# Initialize an empty string to build the pyramid
pyramid = ""

# Loop through each letter in your name
for letter in myName:
    pyramid += letter  # Add the current letter to the pyramid string
    print(pyramid)    # Print the pyramid string

"""
output
enter the name:SAI
S
SA
SAI
"""
