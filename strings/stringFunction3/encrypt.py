# Define a function to decrypt the input string
def decrypt_string(encrypted_str):
    # Initialize an empty string to store the decrypted result
    decrypted_str = ""
    
    # Initialize an index variable to iterate through the input string
    i = 0
    
    # Start a loop to iterate through the input string
    while i < len(encrypted_str):
        # Extract the current character at index 'i'
        char = encrypted_str[i]
        
        # Check if the character is alphabetic 
        if char.isalpha():
            # Initialize an empty string to collect consecutive alphabetic characters
            char_group = ""
            
            # Collect consecutive alphabetic characters
            while i < len(encrypted_str) and encrypted_str[i].isalpha():
                char_group += encrypted_str[i]  # Append the character to the char_group
                i += 1  # Move to the next character
            
            # Initialize a variable to store the number of times to repeat the char_group
            repeat = 0
            
            # Collect consecutive digits to determine the repeat count
            while i < len(encrypted_str) and encrypted_str[i].isdigit():
                repeat = repeat * 10 + int(encrypted_str[i])  # Convert digits to an integer
                i += 1  # Move to the next character
            
            # If no repeat count is provided, default to 1
            if repeat == 0:
                repeat = 1
            
            # Append the char_group repeated 'repeat' times to the decrypted string
            decrypted_str += char_group * repeat
        else:
            # If the character is not alphabetic (e.g., special character), skip it
            i += 1
    
    # Return the decrypted string and its length
    return decrypted_str, len(decrypted_str)

# Example usage:
encrypted_str = "ac2bd3"
decrypted, length = decrypt_string(encrypted_str)

# Print the decrypted string and its length
print("Decrypted:", decrypted)
print("Length:", length)
