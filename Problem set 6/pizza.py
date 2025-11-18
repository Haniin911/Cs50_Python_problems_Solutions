import sys
import os
import csv
from tabulate import tabulate

args = sys.argv[1:]

# Validate arguments
if len(args) < 1:
    print("Too few command-line arguments")
    sys.exit(1)

if len(args) > 1:
    print("Too many command-line arguments")
    sys.exit(1)

filename = args[0]

if not filename.endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

if not os.path.isfile(filename):
    print("File does not exist")
    sys.exit(1)

# Read & print table
with open(filename, newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)

# If file is empty or missing header
if len(rows) == 0:
    print("CSV file is empty")
    sys.exit(1)

print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))
