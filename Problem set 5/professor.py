import random



def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        tries = 0
        while tries < 3:
            try:
                user = int(input(f"{x} + {y} = "))
                if user == answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1

        if tries == 3:
            print(f"{x} + {y} = {answer}")

    print("Score:", score)



def get_level():
    while True:
        try:
            n=int(input("Level: "))
            if n!=1 and n!=2 and n!=3:
                raise ValueError
        except ValueError:
            pass
        else:
            return n
            break

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
