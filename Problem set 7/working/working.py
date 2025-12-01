import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$'
    match = re.fullmatch(pattern, s.strip())
    if not match:
        raise ValueError("Invalid format")


    h1, m1, period1, h2, m2, period2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0


    if not (1 <= h1 <= 12) or not (0 <= m1 < 60):
        raise ValueError("Invalid time")
    if not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError("Invalid time")

   
    def to_24_hour(h, m, period):
        if period == "AM":
            if h == 12:
                h = 0
        else:  # PM
            if h != 12:
                h += 12
        return f"{h:02d}:{m:02d}"

    start = to_24_hour(h1, m1, period1)
    end = to_24_hour(h2, m2, period2)

    return f"{start} to {end}"

if __name__ == "__main__":
    main()
