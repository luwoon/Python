s = input("Greeting: ").lower()

if s[:5] == "hello":
    print("$0")
elif s[0] == "h" and s[:5] != "hello":
    print("$20")
else:
    print("$100")
