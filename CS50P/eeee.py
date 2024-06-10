# fuel

def main():
    num, den = get_frac()  # Ensure `num` and `den` are obtained from get_frac
    fraction = float(num) / den
    if fraction <= 0.01:
        print("E")
    elif fraction >= 0.99:
        print("F")
    else:
        output = fraction * 100
        print(f"{output}%")

def get_frac():
    while True:
        user_input = input("Fraction: ")
        if "/" in user_input:
            try:
                num, den = user_input.split("/")
                num = int(num)
                den = int(den)
                if den != 0 and num <= den:  # Changed to `<=` to match your initial logic
                    return num, den
            except (ValueError, ZeroDivisionError):
                pass

if __name__ == "__main__":
    main()
