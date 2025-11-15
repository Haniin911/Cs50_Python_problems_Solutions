while True:
    z=input("fraction: ")
    if "/" not in z:
        continue
    x,y=z.split("/")
    try:
        if "." in x or "." in y:
            raise ValueError
        x=int(x)
        y=int(y)
        if x < 0 or x > y:
            raise ValueError
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        res=int(round(x/y,2)*100)
        if res>=99:
            print("F")
        elif res<=0:
            print("E")
        else:
            print(f"{res}%")
        break

