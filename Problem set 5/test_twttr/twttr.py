def main():
    text=input("Input: ")
    s=shorten(text)
    print("Output:",s)

def shorten(word):
    tx=""
    for i in word:
        if i not in ['o','i','u','a','e','A','O','E','I','U']:
           tx+=i
    return tx



if __name__ == "__main__":
    main()
