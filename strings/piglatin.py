# ########## Program 3
# #PigLatin - From the input string, for each word, remove the first, add it to the end of the word
# #and add 'ay' to it.
# #eg I am Python
# #answer Iay maay ythonPay

# inputSentence = #FillinMissingCode
# pigLatinKey = 'ay'
# for word in inputSentence.split(): #gets the word in a sentence
#     #take the first char
#     firstChar = word[0]
#      #FillinMissingCode - check if the word has more than one char

#     word = word[1:] + firstChar + pigLatinKey
#     print( #FillinMissingCode)

# Prompt the user to enter a sentence
inputSentence = input("Enter the string : ")

# Pig Latin key
pigLatinKey = 'ay'

# Loop through each word in the input sentence
for word in inputSentence.split():  # Splitting the input into words

    # Take the first character
    firstChar = word[0]

    # Check if the word has more than one character
    if len(word) > 1:
        # Remove the first character, add it to the end, and add 'ay' to it
        word = word[1:] + firstChar + pigLatinKey
    else:
        # If the word has only one character, just add 'ay' to it
        word = word + pigLatinKey

    # Print the Pig Latin version of the word
    print(word, end=' ')  # Printing with a space separator

# Print a newline to separate the final Pig Latin sentence from the prompt
print()

