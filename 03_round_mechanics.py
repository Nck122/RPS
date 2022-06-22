
def check_rounds() : 

    error = "Please enter a whole number more than 0"

    while True:

        response = input("how many rounds? ")

        if response == "":
            return response

        try:
            # ask the question
            response = int(response)

            # if the amount is too low / to high give
            if response > 0:
               return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissor", "xxx"]

rounds = check_rounds()
rounds_played = 0

choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

# rounds loop starts here
end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        print(heading)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)

    
    user_choice = input(choose_instruction)
    print("you chose {}".format(user_choice))

    if user_choice == "xxx":
        break

    rounds_played += 1

    if rounds_played == rounds:
        end_game = "yes"

