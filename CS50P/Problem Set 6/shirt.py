import os
from PIL import Image, ImageOps
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    valid_ext = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()    

    if input_ext not in valid_ext or output_ext not in valid_ext:
        sys.exit("Invalid input")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(input_file) as infile:
            try_on = wear_shirt(infile)
            try_on.save(output_file)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

def wear_shirt(infile):
    shirt = Image.open("shirt.png")
    size = shirt.size
    new_infile = ImageOps.fit(infile, size)
    new_infile.paste(shirt, (0, 0), shirt)  
    return new_infile


if __name__ == "__main__":
    main()  