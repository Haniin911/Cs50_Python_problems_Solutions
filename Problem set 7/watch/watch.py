import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe[^>]*src="([^"]+)"', s)
    if not match:
        return None

    url = match.group(1)

    pattern = r"^https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)$"
    match = re.match(pattern, url)
    if not match:
        return None

    video_id = match.group(1)
    return f"https://youtu.be/{video_id}"




if __name__ == "__main__":
    main()
