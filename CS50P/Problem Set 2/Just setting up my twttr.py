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


if __name__ == "__main__":
  main()
