text=input("camelCase: ")
s = ""
for i in text:
    if i.isupper():
        s+="_"+i.lower()
    else:
        s+=i

print("snake_case: ", s)
