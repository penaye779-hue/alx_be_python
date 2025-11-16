# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the current row
current_row = 1

# Use while loop to iterate through each row
while current_row <= size:
    # Use for loop to print asterisks in a row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after printing a row
    print()
    # Increment the current row
    current_row += 1
