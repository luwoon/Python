# fuel

def main():
    get_frac()
    if float(num) / den <= 0.01:
        print("E")
    elif float(num) / den >= 0.99:
        print("F")
    else:
        output = num / den * 100
        print(f"{output}%")

def get_frac():
    while True:
        user_input = input("Fraction: ")
        if "/" in user_input:
            try:
                num, den = user_input.split("/")
                num = int(num)
                den = int(den)
                if den != 0 and num < den:
                    return num, den
            except (ValueError, ZeroDivisionError):
                pass

if __name__ == "__main__":
    main()
