"""In this version I use Python's RE tool to help analyse the given string,
work out whether or not it contains numbers, and then separate the string into
amount and item
"""
import re


test_string = [
    "Popcorn",  # String with no number
    "2 pc",  # String with a space then valid number
    "1.50J",  # String with preceding decimal
    "40J",  # String with preceding integer but no space
    ]

for item in test_string:
    # Regular expression to test and find out if an item starts with a number
    number_regex = "^[1-9]"

    # If item has a number, separate the item into two: number and item
    if re.match(number_regex, item):
        amount = int(item[0])
        snack = item[1:]

    # If item has no number, assume number required is 1
    else:
        amount = 1
        snack = item

    # Need to remove white space from around snack
    snack = snack.strip()

    # Print order
    print(f"Amount: {amount}")
    print(f"Snack: {snack}")
    print(f"Length of snack: {len(snack)}")
