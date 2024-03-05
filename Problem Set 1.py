# Hello, name

name = input("What is your name? ")
print(f"hello, {name}")

# Recreate Nintendo’s Super Mario Brothers's pyramid using hashes (#), allowing users to state height of pyramid

while True:
    try:
        height = int(input("Height: "))
        if height < 9 and height > 0:
            break
    except ValueError:
        print("Please enter an integer.")

def print_row():
    for i in range(1, height + 1):
        print(" " * (height - i) + "#" * i + "  " + "#" * i + " " * (height - i))

print_row()

# Return minimum number of coins (25, 10, 5, or 1 cent-coins) to make up stated amount of change in cents

from cs50 import get_float

change = -1
while change < 0:
    change = get_float("Change: ") * 100

ncoin = 0
while change >= 25:
    change -= 25
    ncoin += 1
while change >= 10:
    change -= 10
    ncoin += 1
while change >= 5:
    change -= 5
    ncoin += 1
while change >= 1:
    change -= 1
    ncoin += 1

print(ncoin)

# Check validity of Mastercard, Visa, and Amex numbers

number = input("Number: ")
length = len(number)

def main():
    product = every_other(number)
    product_sum = digit_sum(product)
    remaining_sum_val = remaining_sum(number)
    final = remaining_sum_val + product_sum
    if final % 10 != 0:
        print("INVALID")
    else:
        if (int(number) >= 340000000000000 and int(number) <= 349999999999999)  or (int(number) >= 370000000000000 and int(number) <= 379999999999999):
            print("AMEX")
        elif (int(number) >= 5100000000000000 and int(number) <= 5599999999999999):
            print("MASTERCARD")
        elif (int(number) >= 4000000000000 and int(number) <= 4999999999999) or (int(number) >= 4000000000000000 and int(number) <= 4999999999999999):
            print("VISA")

def every_other(number):
    product = ""
    if length % 2 == 0: # even number of digits
        for digit in range(0, length, 2):
            doubled = int(number[digit]) * 2
            product += str(doubled)
    elif length % 2 == 1: #odd number of digits
        for digit in range(1, length, 2):
            doubled = int(number[digit]) * 2
            product += str(doubled)
    return(product)

def digit_sum(number):
    sum = 0
    for digit in number:
        sum += int(digit)
    return(sum)

def remaining_sum(number):
    sum = 0
    if length % 2 == 0: # even number of digits
        for digit in range(1, length, 2):
            sum += int(number[digit])
    elif length % 2 == 1: #odd number of digits
        for digit in range(0, length, 2):
            sum += int(number[digit])
    return(sum)

main()

# Readability test based on Coleman-Liau index 

text = input("Text: ")

def main():
    words = word_count(text)
    sentences = sentence_count(text)
    letters = letter_count(text)
    avg_letters = letters / words * 100
    avg_sentences = sentences / words * 100
    index = 0.0588 * avg_letters - 0.296 * avg_sentences - 15.8
    if index < 1.5:
        print("Before Grade 1")
    elif index >= 16.0:
        print("Grade 16+")
    else:
        rounded_index = round(index)
        print(f"Grade {rounded_index}")

def word_count(text):
    n_words = 1
    for char in text:
        if char == " ":
            n_words += 1
    return(n_words)

def sentence_count(text):
    n_sentences = 0
    for char in text:
        if char == "." or char == "!" or char == "?":
            n_sentences += 1
    return(n_sentences)

def letter_count(text):
    text = text.lower()
    n_letters = 0
    for char in text:
        if char >= 'a' and char <= 'z':
            n_letters += 1
    return(n_letters)

main()

# Program to identify to whom a sequence of DNA belongs

import csv
import sys

def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Please input exactly two command-line arguments.")
        sys.exit(1)

    # Read database file into a variable
    database = []
    database_filename = sys.argv[1]
    with open(database_filename) as file:
        reader = csv.DictReader(file)
        n_STR = len(reader.fieldnames) - 1
        for row in reader:
            database.append(row)

    # Read DNA sequence file into a variable
    sequence_filename = sys.argv[2]
    with open(sequence_filename) as file:
        sequence = file.read()

    # Find longest match of each STR in DNA sequence
    STR_dict = {}
    for str_key in reader.fieldnames:
        STR_dict[str_key] = longest_match(sequence, str_key)

    # Check database for matching profiles
    for person in database:
        match = True
        for key, value in person.items():
            if key != 'name' and int(value) != STR_dict[key]:
                match = False
                break
        if match:
            print(person['name'])
            break
    else:
        print("No match")

    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

main()
