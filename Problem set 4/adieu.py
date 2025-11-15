ls = []

# Take input until EOF
while True:
    try:
        text = input()
        ls.append(text)
    except EOFError:
        break

res = "Adieu, adieu, to "

if len(ls) == 1:
    res += ls[0]
elif len(ls) == 2:
    res += f"{ls[0]} and {ls[1]}"
else:
    res += ", ".join(ls[:-1]) + f", and {ls[-1]}"

print(res)
