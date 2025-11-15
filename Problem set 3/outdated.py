ls = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        text = input("Date: ").strip()

        if "," in text:  # format like "September 8, 2025"
            m, d, y = text.split()
            d = d.replace(",", "")
        elif "/" in text:
            m, d, y = text.split("/")
            if m.isalpha():
                raise ValueError
        else:
            raise ValueError

        d = int(d)
        y = int(y)

        if d < 1 or d > 31:
            raise ValueError

        if m.isdigit():
            m = int(m)
            if m < 1 or m > 12:
                raise ValueError
        else:
            m = m.title()
            if m not in ls:
                raise ValueError
            m = ls.index(m) + 1

        # format with leading zeros
        mo = f"{m:02d}"
        da = f"{d:02d}"

    except ValueError:
        continue
    else:
        print(f"{y}-{mo}-{da}")
        break
