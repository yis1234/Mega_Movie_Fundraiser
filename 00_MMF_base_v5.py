"""Added 03_age_validator_v4
"""


# Import statements

# Functions go here

# Check that the ticket name is not blank
def check_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():
            print("Error – please enter a name.")
        else:
            return response


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
            print("Sorry,", name, "is too young for this movie")
            break
        elif int(age) > MAX_AGE:
            print("Sorry,", name, "is too old for this movie")
            break
    return age


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and show instructions
# if necessary

# Loop to get ticket details
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count < MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left.")
    else:
        # Warns the user there is only one seat left
        print(f"\n***** You have ONLY ONE seat left! *****")
    # get details
    name = check_blank("Please enter your name: ")
    if name != "Xxx":
        age = age_validator()
        if 12 <= int(age) <= 110:
            count += 1  # don't want to include escape code in the count

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still"
          f" {MAX_TICKETS - count} tickets left")
else:
    print(f"\nYou have sold all the available tickets")

    # Get age (between 12 and 110)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file
