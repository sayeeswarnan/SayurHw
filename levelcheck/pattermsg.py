from collections import Counter

def encode_message(message, pattern):
    encoded_message = []
    message_index = 0

    for char in pattern:
        if char == '*':
            if message_index < len(message):
                encoded_message.append(message[message_index])
                message_index += 1
            else:
                encoded_message.append(' ')
        else:
            encoded_message.append(char)

    return ''.join(encoded_message)

def count_words(sentence):
    words = sentence.split()
    word_count = Counter(words)
    return word_count

message = "I Love India"
pattern = "*** **** ** **********     *****"


# Encode the message using the pattern
encoded_output = encode_message(message, pattern)

# Count the occurrences of each word in the encoded message
word_counts = count_words(encoded_output)

# Print the encoded message and word counts
print("Encoded Message:")
print(encoded_output)

print("\nWord Counts in Encoded Message:")
for word, count in word_counts.items():
    print(f"{word}: {count}")



