def check_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# main routine
name = check_blank("What is your name? ", "Error – you must enter a name.")

