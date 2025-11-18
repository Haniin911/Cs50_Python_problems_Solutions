import sys
import os
import csv


args = sys.argv[1:]

# Validate arguments
if len(args)<2 :
    print("Too few command-line arguments")
    sys.exit(1)

if len(args)>2:
    print("Too many command-line arguments")
    sys.exit(1)

if not args[0].endswith(".csv") or not args[1].endswith(".csv"):
    print("Could not read invalid_file.csv")
    sys.exit(1)

if not os.path.isfile(args[0]):
    print("Could not read invalid_file.csv")
    sys.exit(1)
students=[]
with open(args[0]) as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"] ,"house":row["house"]})

newStudent=[]


for st in students:
    first, last = [x.strip() for x in st["name"].split(",")]
    house = st["house"]
    newStudent.append({"first": first, "last": last, "house": house})


with open(args[1],"a") as file:
   writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
   if file.tell() == 0:
       writer.writeheader()
   for st in newStudent:
       writer.writerow({"first":st['first'],"last":st['last'],"house":st['house']})

