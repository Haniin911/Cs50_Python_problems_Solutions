import random
while True:
    try:
        n=int(input("Level: "))
        if n<1:
            raise ValueError
    except ValueError:
        pass
    else:
        break
x=random.randint(1,n)
while True:
    try:
        t=int(input("Guess: "))
        if t>n or t>x:
            print("Too large!")
            raise ValueError
        elif t<1:
            raise ValueError
        elif t<x:
            print("Too small!")
            raise ValueError
    except ValueError:
        pass
    else:
        if t==x:
            print("Just right!")
        break




