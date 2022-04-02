""" Testing if the first or second character in a string is a number.
In this program all I have done is try an alternative method
of splitting the first 1 or 2 characters off from the rest of the string
"""


test_string = [
    "Popcorn",  # String with no number
    "2 pc",  # String with a space then valid number
    "1.50J",  # String with preceding decimal
    "40J",  # String with preceding integer but no space
    "12Chips",
    ]

for item in test_string:
    if item[0].isdigit():  # Test to see if first char is a digit
        if item[1].isdigit():  # If so, what about the second char
            quantity = int(item[0] + item[1])  # If both are digits, join them
            snack = item[2:]  # and split the rest of the string off at item 2
        else:
            quantity = int(item[0])  # If only the first char is a digit
            snack = item[1:]  # Split the rest of the string off at item 1
    else:  # If no digit is found
        quantity = 1  # assume quantity is 1
        snack = item
    print(f"Quantity = {quantity}")
    print(f"Snack = {snack}")
