def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not s[0].isalpha() and not s[1].isalpha():
            return False
    flag=False
    for i in range(1, len(s)):
        if not flag:
            if s[i].isdigit():
                if s[i]=="0":
                    return False
                else:
                    flag = True
            elif not s[i].isalpha():
                return False
        else:
            if not s[i].isdigit():
                return False

    return True




if __name__=="__main__":
    main()
