import random

def main():
    level = get_level()
    random_int = random.randint(1, level)
    guess(random_int)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
              return level
        except ValueError:
            pass
        

def guess(random_int):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == random_int:
                print("Just right!")
                break
            elif guess < random_int:
                print("Too small!")
            elif guess > random_int:
                print("Too big!")
        except ValueError:
            pass


if __name__ == "__main__":
    main() 
