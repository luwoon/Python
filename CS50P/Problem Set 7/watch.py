import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    route = None
    matches = re.search(r'<iframe .*src="https?://(www\.)?youtube\.com/embed/([^"]+)".+</iframe>', s)
    if matches:
        route = matches.group(2)
    if route != None:
      return f"https://youtu.be/{route}"
    else:
      return None


if __name__ == "__main__":
    main()