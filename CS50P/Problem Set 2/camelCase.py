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


if __name__ == "__main__":
  main()
