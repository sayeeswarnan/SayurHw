# Initialize variables
redBags, whiteBags = 100, 200
totalSales, totalBagsSold = 0, 0

while totalSales < 10000 and totalBagsSold < 10:
    # Ask the customer for input
    red_to_sell = int(input("How many red bags would you like to buy? "))
    white_to_sell = int(input("How many white bags would you like to buy? "))
    
    # Calculate the total cost for the bags
    totalCost = (red_to_sell * 1000) + (white_to_sell * 1500)
    
    # Check if there are enough bags to sell
    if red_to_sell > redBags or white_to_sell > whiteBags:
        print("Sorry, we don't have enough bags in stock.")
        continue
    
    redBags -= red_to_sell  # Deduct red bags from stock
    whiteBags -= white_to_sell  # Deduct white bags from stock
    
    # Increment the number of bags sold and update total sales
    bags_to_sell = red_to_sell + white_to_sell
    totalBagsSold += bags_to_sell
    totalSales += totalCost

    print("You bought", red_to_sell, "red bags and", white_to_sell, "white bags for Rs", totalCost)
    print("Total Sales: Rs", totalSales)
    print("Total Bags Sold:", totalBagsSold)

print("Program ended. Total Sales:", totalSales, "Total Bags Sold:", totalBagsSold)