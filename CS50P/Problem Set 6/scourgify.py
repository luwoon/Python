import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    new_rows = []

    try:
        with open(input_file) as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                last, first = row["name"].split(", ")
                new_rows.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


    with open(output_file, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(new_rows)

    
if __name__ == "__main__":
    main()