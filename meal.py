def main():
    text=input("What time is it? ")
    time=convert(text)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(text):
    hours, minutes = text.split(":")
    hours = int(hours)
    minutes = int(minutes)
    time_float = hours + (minutes / 60)
    return time_float


if __name__ == "__main__":
    main()
