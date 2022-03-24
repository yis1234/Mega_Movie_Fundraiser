"""Based on 06_string_validator_v2, this program uses the string validator
function to ask if the user wants to order snacks. If the response is 'yes',
the function is called repeatedly to check that the choice of snack is valid.
The user chooses 'x' to stop ordering snacks.
"""


def get_choice(question, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    choice = input(question).lower()
    for item in valid_choices:
        if choice in item:
            choice = item[0].title()
            return choice

    print(choice_error)
    return get_choice(question, valid_choices)


# Main routine
ask_for_snack = "What snack do you want – 'x' to stop ordering: "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "p", "c", "3"],
                ["water", "w", "4"], ["x"]]

check_snacks = "Do you want snacks: "
valid_yes_no = [["y", "yes"], ["n", "no"]]

getting_snacks = True
snacks_required = get_choice(check_snacks, valid_yes_no)
while getting_snacks:
    if snacks_required == "N":
        print("You don't want snacks")
        getting_snacks = False
    else:
        option = get_choice(ask_for_snack, valid_snacks)
        if option != "X":
            print(f"You have chosen {option}")
        else:
            getting_snacks = False
            print("Thanks for ordering your snacks")




