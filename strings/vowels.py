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








