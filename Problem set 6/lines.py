import sys
import os
params=[]
for arg in sys.argv[1:]:
    params.append(arg)

if len(params) > 1:
    print("Too many command-line arguments")
    sys.exit(1)
elif len(params) == 0:
    print("Too few command-line arguments")
    sys.exit(1)
elif not params[0].endswith(".py"):
    print("Not a Python file")
    sys.exit(1)
elif not os.path.isfile(params[0]):
    print("File does not exist")
    sys.exit(1)
else:
    lines=[]
    with open(params[0]) as file:
        for line in file:
            l=line.strip()
            if l=="":
                continue
            if l.startswith("#"):
                continue
            lines.append(l)

        print(len(lines))


