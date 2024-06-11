import re

dict = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

format1 = r'^\d{1,2}/\d{1,2}/\d{4}$'
format2 = r'^(' + '|'.join(dict) + r') \d{1,2}, \d{4}$'


def main():
    m, d, y = extract()
    print(f"{y}-{int(m):02d}-{int(d):02d}")


def extract():
  while True:
    date = input("Date: ")
    if re.match(format1, date):
        try:
            m, d, y = date.split("/")
            if int(m) > 12 or int(d) > 31:
                pass
            else:
              return m, d, y
        except ValueError:
            pass
    elif re.match(format2, date):
        try:
            month, day, y = date.split()
            if int(day) > 31 or month not in dict:
                pass
            else:
              m = dict.index(month) + 1
              d = day.rstrip(",")
              return m, d, y
        except ValueError:
            pass
        

if __name__ == "__main__":
    main()
