def check_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("Error – you must enter a name.")
        else:
            return response


# main routine
name = check_blank("What is your name? ")
