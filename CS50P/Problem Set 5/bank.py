def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    if greeting[:5].lower() == "hello":
        return "$0" 
    elif greeting[0].lower() == "h" and greeting[:5].lower() != "hello":
        return "$20" 
    else:
        return "$100"


if __name__ == "__main__":
    main()