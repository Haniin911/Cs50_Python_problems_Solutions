def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    x, y = fraction.split("/")

    if "." in x or "." in y:
        raise ValueError

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or x > y:
        raise ValueError

    return int(round((x / y) * 100))


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
