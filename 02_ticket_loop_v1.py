# start of loop

# initialize loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    # get details
    name = input("Please enter your name: ").title()
    count += 1
