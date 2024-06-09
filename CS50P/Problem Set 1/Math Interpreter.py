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


if __name__ == "__main__":
  main()
