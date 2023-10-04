# 3. Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
# Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
# Do not use dictionaries. Try to use string built in functions.



# Define a function named mostFrequentLetters that takes a string 's' as input
def mostFrequentLetters(s):
    # Convert the input string s to lowercase
    s = s.lower()

    # Define a string containing all lowercase letters of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Create a list of tuples with each tuple containing a letter and its count in s
    # Only include letters with a count greater than 0
    letter_counts = [(ch, s.count(ch)) for ch in alphabet if s.count(ch) > 0]
   
    
   # Sort the list of tuples in descending order of count and ascending order of letters
    letter_counts.sort(key=lambda x: (-x[1], x[0]))
    #-x[1] negates the count. This means that if two elements have the same count, the one with the higher count will come first.
    #x[0] refers to the first element of the tuple x, which is the letter itself. 
    

    for ch, count in letter_counts:
        print(ch, end='')
    return ch   
   

# Call the mostFrequentLetters function with the input string "We Attack at Dawn"
result = mostFrequentLetters("We Attack at Dawn")

# Print the result
print(result)  # Output: 'atwcdekn'

