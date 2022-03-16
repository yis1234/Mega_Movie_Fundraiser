""" Integer checking function – loops until a valid number is entered
this version uses .isdigit() to check for a valid integer
"""


def age_validator(age):
    # Get user age
    while True:
        if age.isdigit():
            # check if age is between 12 and 110
            if 12 <= int(age) <= 110:
                return age
            else:
                age = input("Age must be between 12 and 110"
                            "\n\nPlease enter the age of the ticket holder: ")
        else:
            age = input("Please enter an integer (i.e. a whole number "
                        "with no decimals)"
                        "\n\nPlease enter the age of the ticket holder: ")


age_ = age_validator(input("\nPlease enter the age of the ticket holder: "))
print(f"Age = {age_}")
