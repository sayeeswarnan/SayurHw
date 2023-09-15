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

inputSentence = input("Enter the string : ")
inputSentence=inputSentence 
pigLatinKey = 'ay' #set piglatinkey
vowels = ['a','e','i','o','u','A','E','I','O','U']#set vowels on list
words=inputSentence.split(" ") #spliting the sentences into words 
sentence=""#set empty string 
for word in words: #gets the word in a sentence
   
    first_vowel_index = 0
    #FillinMissingCode - check if the word has more than one char
    for index, char in enumerate(word): #returns both the index and the char in the word
        if char in vowels: 
            first_vowel_index = index
            break
    # string slicing to add words 

    sentence = sentence + word[first_vowel_index+1:] +word[:first_vowel_index + 1] + pigLatinKey #adding  ay at end
    sentence+=" "   # adding space at end of each word
print(f"Final sentence is : {sentence}")
