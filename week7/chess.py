
# Defining the size of the chessboard (8x8)
board_size = 8

# Loop through rows
for row in range(board_size):
    # Loop through columns
    for col in range(board_size):
        # Check if the sum of the row and column indexes is even
        if (row + col) % 2 == 0:
            # Printing a white square
            print('\u25A0', end=' ')
        else:
            # Printing a black square if 'if' condition is false
            print('B', end=' ')
    # Move to the next row
    print()

