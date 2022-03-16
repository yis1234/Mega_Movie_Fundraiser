""" Integer checking function – same as version 3 except it prints you're too
young or too old if you are under the age of 12 or older than 110
"""


def age_validator():
    MIN_AGE = 12
    MAX_AGE = 110
    age = input("Please enter the age of the ticket holder: ")
    while age.isdigit() is False or int(age) < MIN_AGE or int(age) > MAX_AGE:
        if age.isdigit() is False:
            age = input("Please enter an integer (i.e. a whole number "
                        "with no decimals)"
                        "\n\nPlease enter the age of the ticket holder: ")
        elif int(age) < MIN_AGE:
            print("You are too young to be on this ride")
            break
        elif int(age) > MAX_AGE:
            print("You are too old to be on this ride")
            break
    return age


print("Age =", age_validator())
