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
