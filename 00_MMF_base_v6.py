"""Added 04_calculate_ticket_price_v4
Also includes total profit calculations in the main routine
Have changed the variable 'count' to 'ticket_count' and made the formatting
and language in the print statement easier to understand
"""


# Import statements

# Functions go here
# Calculate the ticket price (based on any given age)
def calculate_ticket_price(age):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        ticket_price = child_price
    elif age in standard_age:
        ticket_price = standard_price
    else:
        ticket_price = retired_price

    return(ticket_price)


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
    age = input("Please enter the age of the ticket-holder: ")
    while age.isdigit() is False or int(age) < MIN_AGE or int(age) > MAX_AGE:
        if age.isdigit() is False:
            age = input("Please enter an integer (i.e. a whole number "
                        "with no decimals)"
                        "\n\nPlease enter the age of the ticket-holder: ")
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
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0

while name != "Xxx" and ticket_count < MAX_TICKETS:
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nThere are {MAX_TICKETS - ticket_count} tickets left.")
    else:
        # Warns the user there is only one seat left
        print(f"\n***** There is ONLY ONE seat left! *****")
    # get details
    name = check_blank("Enter ticket-holder's name: ")
    if name != "Xxx":
        age = age_validator()
        if 12 <= int(age) <= 110:
            ticket_count += 1  # don't want to include escape code in the ticket_count
    # Calculate ticket price
        ticket_price = calculate_ticket_price(int(age))
        if 12 <= int(age) <= 110:
            print(f"For {name} the price is ${ticket_price:,.2f}")
            profit += (ticket_price - TICKET_COST_PRICE)

# Calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1: # Making sure it reads OK when only one ticket sold
        print(f"\n{ticket_count} tickets have now been sold")
    else:
        print(f"\n1 ticket has now been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"\n{MAX_TICKETS - ticket_count} tickets are still available")
    else:
        print(f"1 ticket is still available") # Making sure it reads OK when
        # only one ticket left
else:
    print("\n!!!!! All the available tickets have now been sold! !!!!!")
    print("*" * 60)

print(f"Ticket profit is ${profit:,.2f}")

    # Get age (between 12 and 110)

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Output data to text file
