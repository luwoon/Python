import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        pass


def convert(s):
    matches = re.match(r"^(([1-9]|1[0-2])(:[0-5][0-9])?) ((A|P)M) to (([1-9]|1[0-2])(:[0-5][0-9])?) ((A|P)M)$", s)
    if not matches:
        raise ValueError("Invalid time")
    
    start_time = matches.group(1)
    start_period = matches.group(4)
    end_time = matches.group(6)
    end_period = matches.group(9)
        
    start_24 = to_24_hour(start_time, start_period)
    end_24 = to_24_hour(end_time, end_period)
    
    return f"{start_24} to {end_24}"


def to_24_hour(time_str, period):
    parts = time_str.split(':')
    hour = int(parts[0])
    minute = parts[1] if len(parts) > 1 else "00"

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    if not (0 <= hour <= 23 and 0 <= int(minute) <= 59):
        raise ValueError("Invalid time")

    return f"{hour:02}:{minute}"


if __name__ == "__main__":
    main()