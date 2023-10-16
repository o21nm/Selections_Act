def chinese_zodiac(year):
    zodiac_signs = [
        "Monkey", "Rooster", "Dog", "Pig",
        "Rat", "Ox", "Tiger", "Rabbit",
        "Dragon", "Snake", "Horse", "Goat"
    ]

    if year < 1900:
        return "Year before the Chinese zodiac started"

    year_diff = (year - 1900) % 12
    return zodiac_signs[year_diff]


try:
    birth_year = int(input("Enter your birth year: "))
    zodiac = chinese_zodiac(birth_year)
    print(f"Your Chinese zodiac sign is {zodiac}.")
except ValueError:
    print("Please enter a valid year (e.g., 1985).")
