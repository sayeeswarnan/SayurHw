# 1. Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
# When the customer comes in, vendor asks "What do you want to buy?" .
# The customer can say "I want apple", or "Apple" or "three apple" or something like that.
# Your program will find out what fruit the customer is asking. 
# Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
# Print the quantity if the customer says the quantity. If not, ask him how much he wants.
# Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
# You can limit the quantity to single digit number.

def extract_fruit_quantity(input_str):
    input_str = input_str.lower()
    fruits = ['apple', 'orange', 'banana']
    words = input_str.split()
    
    for word in words:
        if word.isdigit() and int(word) < 10:
            quantity = int(word)
            for fruit in fruits:
                if fruit in input_str:
                    return fruit.capitalize(), quantity
    
    for fruit in fruits:
        if fruit in input_str:
            quantity = int(input(f"How many {fruit}s do you want? (Please enter a single-digit number) "))
            return fruit.capitalize(), quantity
    
    return None, None

def main():
    customer_input = input("What do you want to buy? ").strip()
    fruit, quantity = extract_fruit_quantity(customer_input)
    
    if fruit:
        print(f"You want {quantity} {fruit}s.")
    else:
        print("Sorry, I don't understand what you want.")

if __name__ == "__main__":
    main()
