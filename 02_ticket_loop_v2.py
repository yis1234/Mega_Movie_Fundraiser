"""This version includes a print statement after the name, saying how many
tickets are still available for sale
"""

# initialize loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    # get details
    name = input("Please enter your name: ").title()
    if name != "Xxx":
        count += 1
        print(f"You have {MAX_TICKETS - count} seats left")
if count == MAX_TICKETS:
    print("You have sold all the available tickets")
else:
    print(f"You have sold {count} tickets")
    print(f"There are still {MAX_TICKETS - count} available")

