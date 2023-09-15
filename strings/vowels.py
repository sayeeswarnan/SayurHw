# ########## Program 4
# #PigLatin - From the input string, for each word, remove the first chars until a vowel, add it to the end of the word
# #and add 'ay' to it.
# #eg I am Python
# #answer Iay maay nPythoay (in Python 'o' is the first vowel)

# inputwords = #FillinMissingCode
# pigLatinKey = 'ay'
# vowels = ['a','e','i','o','u']

# for word in inputwords.split(): #gets the word in a words
#     #take the first chars until a vowel
#     first_vowel_index = 0
#     #FillinMissingCode - check if the word has more than one char
#     for index, char in enumerate(word): #returns both the index and the char in the word
#          #FillinMissingCode - check if the char is vowel or not
        
     

#     word = #FillinMissingCode  
#     print( #FillinMissingCode)
inputwords = input("Enter the string : ")
inputwords=inputwords 
pigLatinKey = 'ay' #set piglatinkey
vowels = ['a','e','i','o','u','A','E','I','O','U']#set vowels on list
words=inputwords.split(" ") #spliting the wordss into words 
words=""#set empty string 
for word in words: #gets the word in a words
    #take the first chars until a vowel
    first_vowel_index = 0
    #FillinMissingCode - check if the word has more than one char
    for index, char in enumerate(word): #returns both the index and the char in the word
        if char in vowels: 
            first_vowel_index = index
            break
    # here using string slicing to add words in String

    words = words + word[first_vowel_index+1:] +word[:first_vowel_index + 1] + pigLatinKey    # finally adding the ay at end
    words+=" "   # adding space at end of each word
print(f"Final words is : {String}")






# inputwords = "I am Python"  # Example input words
# pigLatinKey = 'ay'
# vowels = ['a', 'e', 'i', 'o', 'u']

# # Split the input words into words
# for word in inputwords.split():
#     # Initialize the index of the first vowel
#     first_vowel_index = 0

#     # Check if the word has more than one character
#     if len(word) > 1:
#         # Iterate through the characters of the word
#         for index, char in enumerate(word):
#             # Check if the character is a vowel
#             if char.lower() in vowels:
#                 first_vowel_index = index
#                 break  # Exit the loop when the first vowel is found

#     # Apply Pig Latin transformation to the word
#     if first_vowel_index > 0:  # Check if there is at least one vowel in the word
#         prefix = word[:first_vowel_index]  # Get the characters before the first vowel
#         rest_of_word = word[first_vowel_index:]  # Get the characters from the first vowel onwards
#         pigLatinWord = rest_of_word + prefix + pigLatinKey  # Form the Pig Latin word
#     else:
#         # If there are no vowels in the word, treat it as a special case
#         pigLatinWord = word + pigLatinKey

#     # Print the Pig Latin word with a space
#     print(pigLatinWord, end=" ")

