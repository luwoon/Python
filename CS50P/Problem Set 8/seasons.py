from datetime import date, datetime, timedelta
import inflect
import sys


def main():
    dob = get_dob()
    diff = minutes(dob)
    output = to_words(diff).capitalize()
    print(f"{output} minutes")


def get_dob():
    while True:
        user_input = input("Date of Birth: ")
        try:
            dob = datetime.strptime(user_input, "%Y-%m-%d").date()
            return dob
        except ValueError:
            sys.exit("Invalid date")

def minutes(dob):
    today = date.today()
    difference = today - dob
    return difference.days * 24 * 60

def to_words(diff):
    p = inflect.engine()
    return p.number_to_words(diff)


if __name__ == "__main__":
    main()