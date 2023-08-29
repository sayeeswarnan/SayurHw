############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.
total_money = 0
ask_count = 0

while total_money < 1000 and ask_count < 5:#while total_money < 1000 and ask_count < 5:: This starts a while loop that continues as long as two conditions are met:
    money_given = float(input("How much money did your parents give you this time? Rs "))
    
    if money_given <= 10:#if money_given <= 10:: This line checks if the money_given is less than or equal to Rs 10.
        continue  # Skip this iteration if money_given is less than or equal to Rs 10
    
    total_money += money_given
    ask_count += 1
    print(f"You have received Rs {total_money} so far. Thank you.")

if total_money >= 1000:
    print(f"You have collected enough money to go to the movies! It took you {ask_count} attempts.")
else:
    print(f"Sorry, you couldn't collect enough money to go to the movies after {ask_count} attempts.")
