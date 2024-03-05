# Hello, name

name = input("What is your name? ")
print(f"hello, {name}")

# Recreate Nintendo’s Super Mario Brothers's pyramid using hashes (#), allowing users to state height of pyramid

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

# Return minimum number of coins (25, 10, 5, or 1 cent-coins) to make up stated amount of change in cents

from cs50 import get_float

change = -1
while change < 0:
    change = get_float("Change: ") * 100

ncoin = 0
while change >= 25:
    change -= 25
    ncoin += 1
while change >= 10:
    change -= 10
    ncoin += 1
while change >= 5:
    change -= 5
    ncoin += 1
while change >= 1:
    change -= 1
    ncoin += 1

print(ncoin)

# Check validity of Mastercard, Visa, and Amex numbers

number = input("Number: ")
length = len(number)

def main():
    product = every_other(number)
    product_sum = digit_sum(product)
    remaining_sum_val = remaining_sum(number)
    final = remaining_sum_val + product_sum
    if final % 10 != 0:
        print("INVALID")
    else:
        if (int(number) >= 340000000000000 and int(number) <= 349999999999999)  or (int(number) >= 370000000000000 and int(number) <= 379999999999999):
            print("AMEX")
        elif (int(number) >= 5100000000000000 and int(number) <= 5599999999999999):
            print("MASTERCARD")
        elif (int(number) >= 4000000000000 and int(number) <= 4999999999999) or (int(number) >= 4000000000000000 and int(number) <= 4999999999999999):
            print("VISA")

def every_other(number):
    product = ""
    if length % 2 == 0: # even number of digits
        for digit in range(0, length, 2):
            doubled = int(number[digit]) * 2
            product += str(doubled)
    elif length % 2 == 1: #odd number of digits
        for digit in range(1, length, 2):
            doubled = int(number[digit]) * 2
            product += str(doubled)
    return(product)

def digit_sum(number):
    sum = 0
    for digit in number:
        sum += int(digit)
    return(sum)

def remaining_sum(number):
    sum = 0
    if length % 2 == 0: # even number of digits
        for digit in range(1, length, 2):
            sum += int(number[digit])
    elif length % 2 == 1: #odd number of digits
        for digit in range(0, length, 2):
            sum += int(number[digit])
    return(sum)

main()

