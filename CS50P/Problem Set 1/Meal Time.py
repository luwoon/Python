def main():
    time = input("What time is it? ")
    t = convert(time)
    if 7.0 <= t <= 8.0:
      print("breakfast time")
    elif 12.0 <= t <= 13.0:
      print("lunch time")
    elif 18.0 <= t <= 19.0:
      print("dinner time")
    else:
      pass


def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    t = h + m / 60.0
    return t


if __name__ == "__main__":
    main()
