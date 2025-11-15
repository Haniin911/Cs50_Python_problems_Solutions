ls={}
while True:
    try:
        text=input().upper()
        if text not in ls:
            ls[text]=1
        else:
            ls[text]+=1
    except EOFError:
        break
ls=sorted(ls.items())

for it,val in ls:
    print(f"{val} {it}")


