# Apply figlet font

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()


if len(sys.argv) == 1:
    s = input("Input: ")
    random_font = random.choice(font_list)
    figlet.setFont(font=random_font)
    print(figlet.renderText(s))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
    s = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(s))
else:
    print("Error!")
    sys.exit
