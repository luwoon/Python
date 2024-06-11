import inflect

p = inflect.engine()

list = []

try:
    while True:
        name = input("Name: ").title()
        list.append(name)
except EOFError:
    pass

names = p.join(list)
print(f"Adieu, adieu, to {names}")
