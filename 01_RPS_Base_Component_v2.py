
import random

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


# checks answer is valid (ie: it's in the list of valid responses)
def choice_checker(question, valid_list, error):
     
    valid = False
    while not valid:


        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        else:
            print(error)

print()
print("Welcome to the Rock, Paper, Scissors Game ")


def instructions():

    print("""

**** Rules / Instructions ****

Choose rock / paper / scissors

- Rock beats scissors
- Paper beats rock
- Scissors beats paper

Can you beat the computer?

    """)



    
# ***** MAIN ROUTINE STARTS HERE *******


yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]


rounds_played = 0
mode = "regular"

choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

# ask user if they want to see the instructions...
played_before = choice_checker("Have you played before? ", yes_no_list, "Please enter y / n")
print("You chose", played_before)

if played_before == "no":
    instructions()

rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 10

# rounds loop starts here
end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        rounds += 1
        print(heading)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print(heading)

    # computer chooses from rps list (excluding the last item which is the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)
    

    user_choice = choice_checker("Choose R / P / S: ", rps_list, "Please enter R / P / S")
    print("you chose {}".format(user_choice))

    if user_choice == "xxx":
        break

    rounds_played += 1

    if rounds_played == rounds:
        end_game = "yes"
        


       

