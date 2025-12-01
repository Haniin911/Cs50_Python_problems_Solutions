# seasons.py
from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = get_birthdate()
    minutes = minutes_since(birthdate)
    words = number_to_words(minutes)
    print(f"{words} minutes")

def get_birthdate():
    """Prompt user for a birthdate and validate YYYY-MM-DD format."""
    user_input = input("Date of birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(user_input, "%Y-%m-%d").date()
        return birthdate
    except ValueError:
        sys.exit("Invalid date format")

def minutes_since(birthdate):
    """Return number of minutes since birthdate until today at midnight."""
    today = date.today()
    delta = today - birthdate
    total_minutes = delta.days * 24 * 60
    return total_minutes

def number_to_words(n):
    """Convert number to words with proper commas and hyphens like CS50 expects."""
    words = p.number_to_words(n, andword="")
    words = words.replace(", and", ",")  
    words = words[0].upper() + words[1:]
    return words


if __name__ == "__main__":
    main()
