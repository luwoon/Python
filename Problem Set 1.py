// Hello, name

name = input("What is your name? ")
print(f"hello, {name}")

// Recreate Nintendo’s Super Mario Brothers's pyramid using hashes (#), allowing users to state height of pyramid

while True:
    try:
        height = int(input("Height: "))
        if height < 9 and height > 0:
            break
    except ValueError:
        print("Please enter an integer.")

def print_row():
    for i in range(1, height + 1):
        print(" " * (height - i) + "#" * i + "  " + "#" * i + " " * (height - i))

print_row()

// Return minimum number of coins (25, 10, 5, or 1 cent-coins) to make up stated amount of change in cents


// Check validity of Mastercard, Visa, and Amex numbers


