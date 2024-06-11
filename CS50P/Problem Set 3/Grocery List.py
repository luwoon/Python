from collections import Counter

list = []

while True:
  try:
    item = input().upper()
    list.append(item)
  except EOFError:
    break

counts = Counter(list)
for item, count in counts.items():
  print(f"{count} {item}")
