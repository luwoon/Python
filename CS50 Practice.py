# Apply figlet font

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    random_font = random.choice(font_list)
    figlet.setFont(font=random_font)
    print(figlet.renderText(s))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
    s = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(s))
else:
    print("Error!")
    sys.exit


# Deposit and withdraw from a cookie jar

def main():
    jar = Jar()
    # jar.deposit(5)
    # jar.withdraw(2)
    print(str(jar))

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 5

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError("Deposit must be a non-negative integer.")
        if self._size + n > self._capacity:
            raise ValueError("Exceed jar capacity.")
        self._size += n

    def withdraw(self, n):
        if n < 0 or not isinstance(n, int):
            raise ValueError("Withdraw must be a non-negative integer.")
        if self._size < n:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property

    # Add up prices of order
    def size(self):
        return self._size

main()

# Add up prices of order

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:  # Infinite loop until break
    try:
        item = input("Item: ")
        if not item:
            break
        elif item.title() in menu:
            cost = menu[item.title()]
            total += cost
            print(f"Total: {total:.2f}")
    except EOFError:
        break
