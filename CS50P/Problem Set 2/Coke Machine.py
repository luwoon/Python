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
