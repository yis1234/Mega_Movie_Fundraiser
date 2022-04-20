"""This version checks to see if there is only ONE ticket left and, if so,
produce a more appropriately worded print statement. Also spaces out the
print statements.
"""

# initialize loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count < MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left.")
    else:
        print(f"\nYou have ONLY ONE seat left")
    # get details
    name = input("Please enter your name: ").title()
    if name != "Xxx":
        count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still"
          f" {MAX_TICKETS - count} tickets left")
else:
    print(f"\nYou have sold all the available tickets")

