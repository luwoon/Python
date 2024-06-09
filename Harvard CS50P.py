# convert to lowercase

s = input("")
print(s.lower())


# replacing

s = input("")
s = s.replace(' ', '...')
print(s)


# emojis

s = input("")
s = s.replace(':)', '🙂').replace(':(', '🙁')
print(s)


# e = mc^2

mass = int(input("m: "))
e = mass * 300000000 ** 2
print(f"E: {e}")


# tip calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = float(d[1:])
    return d

def percent_to_float(p):
    p = float(p[:-1])/100
    return p

main()


# if else

s = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

if int(s) == 42 or s == 'forty two' or s == 'forty-two':
  print('Yes')
else:
  print('No')


# seinfeld

s = input("Greeting: ").lower()

if s[:5] == "hello":
  print("$0")
elif s[0] == "h" and s[:5] != "hello":
  print("$20")
else:
  print("$100")


# file extensions

s = input("File name: ").lower()

dict = {
  ".gif": "image/gif",
  ".jpg": "image/jpg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".pdf": "application/pdf",
  ".txt": "text/plain",
  ".zip": "application/zip"
}

for extension, type in dict.items():
  if s.endswith(extension):
    print(type)
    break
else:
    print("application/octet-stream")


# arithmetic

def main():
  s = input("Expression: ")
  x, y, z = s.split(" ")
  x = int(x)
  z = int(z)
  result = math(x, y, z)
  print(f"{result:.1f}")

def math(x, y, z):
  if y == "+":
    return x + z
  elif y == "-":
    return x - z
  elif y == "/":
    return float(x) / z
  elif y == "*":
    return x * z 
  
main()


# meal time

def main():
    time = input("What time is it? ")
    t = convert(time)
    if 7.0 <= t <= 8.0:
      print("breakfast time")
    elif 12.0 <= t <= 13.0:
      print("lunch time")
    elif 18.0 <= t <= 19.0:
      print("dinner time")
    else:
      pass

def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    t = h + m / 60.0
    return t

if __name__ == "__main__":
    main()


# convert camel case to snake skin

def main():
  s = input("camelCase: ")
  s = convert(s)
  print(f"snake_skin: {s}")

def convert(s):
  result = ""
  for index, a in enumerate(s):
    if a.isupper() and index != 0:
      result += '_' + a.lower()
    else:
      result += a.lower()
  return result

main()


# coin machine

amt = 50
valid = [25, 10, 5]

while amt != 0:
  print(f"Amount Due: {amt}")
  inserted = int(input("Insert Coin: "))
  if inserted not in valid:
    continue
  else:
    amt -= inserted
    if amt == 0:
      print("Amount Due: 0")
      break
    else:
      continue


# omit vowels

def main():
  s = input("Input: ")
  output = omit(s)
  print(f"Output: {output}")

def omit(s):
  vowels = ['a', 'e', 'i', 'o', 'u']
  output = ""
  for char in s:
    if char in vowels:
      output += ""
    else:
      output += char
  return output  

main()


# check validity of requested vanity license plate

def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s):
  if 2 <= len(s) <= 6 and s.isalnum():
    if s.isalpha(): 
      return True
    else:
      if s[:2].isalpha() and s[-2:].isdigit():
        for i in range(len(s)):
          if s[i].isdigit():
            if s[i].startswith("0") or s[i:].isalpha():
              return False
            else:
              return True
      else:
        return False
  else:
    return False

main()


# calories of fruits

dict = {
  "apple":"130",
  "avocado":"50",
  "banana":"110",
  "cantaloupe":"50",
  "grapefruit":"60",
  "grapes":"90",
  "honeydew melon":"50",
  "kiwifruit":"90",
  "lemon":"15",
  "lime":"20",
  "nectarine":"60",
  "orange":"80",
  "peach":"60",
  "pear":"100",
  "pineapple":"50",
  "plums":"70",
  "strawberries":"50",
  "sweet cherries":"100",
  "tangerine":"50",
  "watermelon":"80"
}

def main():
  item = input("Item: ").lower()
  cal = func(item, dict)

def func(item, dict):
  if item in dict:
    print(dict[item])
  else:
    return None 
  
if __name__ == "__main__":
  main()
