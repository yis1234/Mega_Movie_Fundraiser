"""Based on 06_string_validator_v4
Includes 07_string_analyser_v3
"""
import re


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


# Main routine
# Valid snacks holds list of all snacks. Each item is itself a list with all
# the acceptable input options for each snack – full name, initials and
# abbreviations, as well as a reference number.
valid_snacks = [["popcorn", "p", "corn", "(1"], ["m&ms", "mms", "m", "mm" "(2"],
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

# After the loop is broken, check for an empty list
if len(snack_order) > 0:  # If there is something in the list, print each item
    print("\nThis is a summary of your order:")
    for item in snack_order:
        print(f"\t{item[0]} {item[1]}")
else:  # Otherwise, print this
    print("No snacks were ordered")
