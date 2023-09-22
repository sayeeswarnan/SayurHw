
# 1. Print the level of the password security and if the password is acceptable
#     Weak - only alphabets or only numbers or only special chars
#     Ok - at least one alphabet, one number and one special char
#     strong - at least three alphabets, two numbers and one special char
#     Very strong - same as strong, but at least 16 count

#     All passwords must be at least 8 chars long. You can use RegEx if you want.


import re

def check_password_strength(password):
    # Define regular expressions for different criteria
    alphabet = r'[a-zA-Z]'
    number = r'[0-9]'
    special_char= r'[@_!#$%^&*()<>?/\|}{~:]'
    
    # Check the length of the password if it is less than 8 
    if len(password) < 8:
        return "Weak - Password is too short"
    
    # Check if the password contains at least one alphabet, one number, and one special character
    if (re.search(alphabet, password) and
        re.search(number, password) and
        re.search(special_char, password)):
        
        # Check if the password meets the "strong" or "very strong" condition
        if (len(re.findall(alphabet, password)) >= 3 and
            len(re.findall(number, password)) >= 2 and
            len(password) >= 16):
            return "Very strong - Password is very strong"
        else:
            return "Strong - Password is strong"
    else:
        return "Ok - Password is okay"

# Ask the user to enter a password
user_password = input("Enter your password: ")

# Checking the strength of the user's password
result = check_password_strength(user_password)
print("Password strength:", result)
