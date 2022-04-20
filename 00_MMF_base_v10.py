"""Based on 00_MMF_base_v9
Needed to fix the missing columns - not being printed inside the movie frame
Also, the money columns need to be rounded tidily. These have been fixed using
the pandas.set_option methods
For testing purposes, added an option asking user if they want to print
all columns
Change payment method in main routine to while loop (to prevent invalid choice)
"""
# Import statements
import re
import pandas  # Might need to install pandas if library does not already exist


# Functions go here
# This function splits snacks into quantity and snack name
# It has to be called before the snack (name) can be evaluated against the
# valid_snacks list
def split_order(choice):
    # Regular expression to test and find out if an item starts with a number
    number_regex = "^[1-9]"

    # If item has a number, separate the item into two: number and item
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]

    # If item has no number, assume number required is 1
    else:
        quantity_required = 1
        snack_name = choice

    # Need to remove white space from around snack
    snack_name = snack_name.strip()
    return quantity_required, snack_name


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# function to collate each order
def collate_order():
    valid_snacks = [["popcorn", "p", "corn", "(1"], ["m&ms", "mms", "m",
                                                     "mm", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "w", "(4"], ["orange juice", "oj", "(5"],
                    ["x", "exit", "(6"]]

    # Valid options for yes/no questions
    valid_yes_no = [["y", "yes"], ["n", "no"]]

    # The snack_order list records the complete order for a single user
    snack_order = []
    # Maximum number of any snack item which can be ordered
    max_number_of_snacks = 4
    # Assumption that every user will want to order snacks
    getting_snacks = True
    while getting_snacks:
        # Firstly, find out whether the user wants to order snacks
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            # Response is passed to the generic string checking function with the
            # list of valid yes/no responses as parameters
            check_snacks = input("Do you want snacks? (Y/N): ").lower()
            snacks_required = get_choice(check_snacks, valid_yes_no)

        if snacks_required == "N":  # But if they don't want any snacks
            getting_snacks = False
            break

        else:
            # Otherwise, for each snack, the generic string checker is called with
            # the 'ask_for_snacks' question and the list of valid snacks as
            # parameters
            option = ""
            while option != "X":
                snack = input("What snack do you want - or 'x' to stop "
                              "ordering: ").lower()
                snack = split_order(snack)
                quantity = snack[0]
                if quantity > max_number_of_snacks:
                    snack = None
                    print("Sorry, the maximum number you can order is 4")
                else:
                    snack = snack[1]
                    option = get_choice(snack, valid_snacks)
                    if option == "X":
                        getting_snacks = False

                    elif option is not None:  # Filters out invalid choices
                        snack_order.append([quantity, option])
    return snack_order


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

    return ticket_price


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


def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"\nThere are {maximum - sold} tickets left.")
    else:
        # Warns the user there is only one seat left
        print(f"\n***** There is ONLY ONE ticket left! *****")


def check_valid_payment_method():
    ask_payment_method = input("How do you want to pay: ").lower()
    valid_payment_methods = [
        ["credit card", "card", "credit", "cc", "cr", "1"],
        ["eftpos", "eft", "pos", "ep", "e" "2"],
        ["cash", "ca", "money", "notes", "coins", "c", "3"]]
    payment_method = get_choice(ask_payment_method, valid_payment_methods)
    return payment_method


# ******** Main Routine ********


# Set up dictionaries / lists needed to hold data
all_names = []
all_tickets = []

# Create separate lists for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

# Put the separate lists above into a master list
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Store surcharge multiplier
surcharge_mult_list = []

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    "Popcorn": popcorn,
    "M&Ms": mms,
    "Pita Chips": pita_chips,
    "Water": water,
    "Orange Juice": orange_juice,
    "Surcharge Multiplier": surcharge_mult_list
}

# Cost of each snack
price_dict = {
    "Popcorn": 2.5,
    "M&Ms": 3,
    "Pita Chips": 4.5,
    "Water": 2,
    "Orange Juice": 3.25,
}
# Ask user if they have used the program before and show instructions
# if necessary

# Loop to get ticket details
SURCHARGE_RATE = 0.05
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0
surcharge = 0

while name != "X" and ticket_count < MAX_TICKETS:
    # get details
    check_max_tickets(MAX_TICKETS, ticket_count)
    name = check_blank("Enter ticket-holder's name: ").title()
    if name != "X":
        age = age_validator()
        if 12 <= int(age) <= 110:
            ticket_count += 1  # don't want to include escape code in the ticket_count
        # Calculate ticket price
        ticket_price = calculate_ticket_price(int(age))
        if 12 <= int(age) <= 110:
            print(f"For {name} the price is ${ticket_price:,.2f}")
            profit += (ticket_price - TICKET_COST_PRICE)
            # add name and price to lists
            all_names.append(name)
            all_tickets.append(ticket_price)

        # Get snacks
        snack_order = collate_order()

        # Assume no snacks have been bought
        for item in snack_lists:
            item.append(0)  # add 0 as the amount for each item

        # print(snack_order)
        for item in snack_order:  # The item only has 2 parts - number and snack
            if len(item) > 0:  # Checking to eliminate any blank orders
                to_find = item[1]  # Gets the snack name for the item ordered
                amount = item[0]  # and sets 'amount' to number ordered
                add_list = movie_data_dict[to_find]  # Matches the snack name to
                # the movie_data_dict
                add_list[-1] = amount  # Appends the number ordered to the end of
                # the dictionary list of quantities ordered eg if the most recent
                # quantity is 3 it would be added to the end of
                # this list: [2, 5, 0, 1, 3]

        # After the loop is broken, check for an empty list
        if len(snack_order) > 0:  # If there is something in the list, print each item
            print("\nThis is a summary of your order:")
            for item in snack_order:
                print(f"\t{item[0]} {item[1]}")
        else:  # Otherwise, print this
            print("No snacks were ordered")

        payment_method = check_valid_payment_method()
        if not payment_method:
            continue

        elif payment_method == "Credit Card":
            surcharge_multiplier = SURCHARGE_RATE

        else:
            surcharge_multiplier = 0

        surcharge_mult_list.append(surcharge_multiplier)

# Calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:  # Making sure it reads OK when only one ticket sold
        print(f"\n{ticket_count} tickets have now been sold")
    else:
        print(f"\n1 ticket has now been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available")
    else:
        print(f"1 ticket is still available")  # Making sure it reads OK when
        # only one ticket left
else:
    print("\n!!!!! All the available tickets have now been sold! !!!!!")
    print("*" * 60)


# print details
print()

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")  # Changes the index to reference
# the names rather than an actual index number

# Create column called 'Sub Total'
# contains price for ticket and snacks
movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame["Surcharge"]
# Shorten column names
movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips",
                                          "Surcharge Multiplier": "SM"})

# Force all columns to be printed
pandas.set_option('display.max_columns', None)

# Display numbers to 2 decimal places
pandas.set_option("display.precision", 2)

print(movie_frame)

# For testing purposes, ask user if they want to see all columns
# If not, just print Ticket, Sub Total, Surcharge, Total columns
print_all = input("Print all columns? (Y for yes): ").upper()
if print_all == "Y":
    print(movie_frame)
else:
    print(movie_frame[["Ticket", "Sub Total", "Surcharge", "Total"]])

print()

# Calculate ticket profit
print(f"Ticket profit is ${profit:,.2f}")

# Output data to text file
