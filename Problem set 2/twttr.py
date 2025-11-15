text=input("Input: ")
s=""
for i in text:
    if i not in ['o','i','u','a','e','A','O','E','I','U']:
        s+=i
print("Output:",s)
