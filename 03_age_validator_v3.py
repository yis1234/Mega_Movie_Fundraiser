""" Integer checking function – third trial method
"""


def age_validator():
    age = input("Please enter the age of the ticket holder: ")
    while age.isdigit() is False or int(age) < 12 or int(age) > 110:
        if age.isdigit() is False:
            age = input("Please enter an integer (i.e. a whole number "
                        "with no decimals)"
                        "\n\nPlease enter the age of the ticket holder: ")
        elif int(age) < 12 or int(age) > 110:
            age = input("Age must be between 12 and 110"
                        "\n\nPlease enter the age of the ticket holder: ")
    return age


print("Age =", age_validator())
