# 2. Check if the username and password is correct. 
#      Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
#      passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
#      name of the company mentioned in the username, followed by any 3 numbers.
#      eg username : myname@sayur.com. password - mnamesay123 


import re
import random

def generate_password(username):
    # Check if the username contains '@' and ends with '.com', '.edu', '.tech', or 'org'.
    if re.match(r'.+@[a-zA-Z]+\.(com|edu|tech|org)$', username):
        # Extract the name of the company from the username.
        company_name = username.split('@')[1].split('.')[0]
       

        # Get the last three letters before '@'
        last_three_letters = username.split('@')[0][-3:]
        print(last_three_letters)

        # Generate a random three-digit number
        random_number = str(random.randint(100, 999))

        # Define the expected password based on the conditions
        expected_password = (
            username[0] +        # First letter of username
            username[2] +        # Third letter of username
            last_three_letters + # Last 3 letters of username before '@'
            company_name[:3] +  # First three letters of the company name
            random_number       # Random three-digit number
        )

        return expected_password

    return "Invalid username format"

# Example usage:
username = input("Enter username: ")

generated_password = generate_password(username)
if generated_password != "Invalid username format":
    print(f"Generated password components based on the username:")
    print(f"1. First letter of username: {generated_password[0]}")
    print(f"2. Third letter of username: {generated_password[1]}")
    print(f"3. Last 3 letters of username before '@': {generated_password[2:5]}")
    print(f"4. First three letters of the company name: {generated_password[5:8]}")
    print(f"5. Random three-digit number: {generated_password[8:]}")

    entered_password = input("Enter the password components in the specified order (e.g., abcxyz123): ")
    if entered_password == generated_password:
        print("Password is correct.")
    else:
        print("Password is incorrect.")
else:
    print("Invalid username format. Please enter a valid username.")



# import re

# def check_username_password(username, password):
#     # Check if the username contains '@' and ends with '.com', '.edu', '.tech', or 'org'.
#     if re.match(r'.+@[a-zA-Z]+\.(com|edu|tech|org)$', username):
       
        
#         # Extract the name of the company from the username.
#         company_name = username.split('@')[1].split('.')[0]
   
  
#         # Check if the password matches the specified pattern.
#         expected_password = (
#             username[0] +        # First letter of username
#             username[2] +        # Third letter of username
#             username[-3:] +     # Last 3 letters of username
#             company_name[:3] +  # First three letters of the company name
#         )
        
#     if re.search(r'\d{3}$',password):



#         return password == expected_password

#     return False

# # Example usage:
# username = "myname@sayur.com"
# password = "mnesay123"  # Corrected password based on the updated criteria



# if check_username_password(username, password):
#     print("Username and password are correct.")
# else:
#     print("Username and password are incorrect.")



