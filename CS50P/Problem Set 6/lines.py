import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].lower().endswith(".py"):
        sys.exit("Not a Python file")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]

    try:
        with open(filename) as file:
            n = count_lines(file)
            print(n)
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(file):
    n = 0
    for line in file:
        if not line.lstrip().startswith("#") and not line.strip() == "":
            n += 1 
    return n

    
if __name__ == "__main__":
    main()