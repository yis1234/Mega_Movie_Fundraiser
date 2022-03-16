"""Further improved the emphasis - drawing the user's attention when there is
only one available seat left
"""

# initialize loop so that it runs at least once
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
    name = input("Please enter your name: ").title()
    if name != "Xxx":
        count += 1  # don't want to include escape code in the count

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets\nThere are still"
          f" {MAX_TICKETS - count} tickets left")
else:
    print(f"\nYou have sold all the available tickets")
