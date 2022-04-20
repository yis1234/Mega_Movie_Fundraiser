"""Based on the string checker used in 00_MMF_base_v8, this programgets the
payment method checks that it's valid so that it can be used to check
for valid choices from any list
"""


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Main routine
SURCHARGE_RATE = 0.05
surcharge = 0
name = input("What is your name: ").title()
while name != "X":
    # Need to get sub_total for testing purposes
    sub_total = float(input("Sub-total: $"))
    ask_payment_method = input("How do you want to pay: ").lower()
    valid_payment_methods = [["credit card", "card", "credit", "cc", "cr", "1"],
                             ["eftpos", "eft", "pos", "ep", "e" "2"],
                             ["cash", "ca", "money", "notes", "coins", "c", "3"]]
    payment_method = get_choice(ask_payment_method, valid_payment_methods)
    if not payment_method:
        name = input("What is your name: ").title()
        continue

    elif payment_method == "Credit Card":
        surcharge = (sub_total * SURCHARGE_RATE)

    total_payable = sub_total + surcharge

    print(f"{name} | Subtotal: ${sub_total:,.2f} | Surcharge: "
          f"${surcharge:,.2f} | The total payable is ${total_payable:,.2f}")
    name = input("What is your name: ").title()
