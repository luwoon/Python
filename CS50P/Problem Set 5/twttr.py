def main():
    s = input("Input: ")
    output = shorten(s)
    print(f"Output: {output}")


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output = ""
    for char in word:
        if char in vowels:
            output += ""
        else:
            output += char
    return output 


if __name__ == "__main__":
    main()