import random

computerNo = random.randint(1, 100)  # You can change the range as needed

attempt = 0
while True:
    userNo = int(input("Guess the number: "))
    attempt += 1

    if userNo < computerNo:
        print("Low")
    elif userNo > computerNo:
        print("High")
    else:
        print("Congratulations! You guessed the number correctly.")
        break

print("User guessed the number in", attempt, "attempts")
