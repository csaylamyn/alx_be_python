# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to handle columns
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing one row
    print()
    row += 1
