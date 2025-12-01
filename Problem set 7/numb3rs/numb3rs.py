import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    oc = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d?|0)"
    pattern = rf"^{oc}\.{oc}\.{oc}\.{oc}$"
    return re.match(pattern, ip) is not None


if __name__ == "__main__":
    main()
