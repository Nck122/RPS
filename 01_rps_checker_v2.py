
# checks user input based on a list.  
# Input can be the list item or the first letter of a list item
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



# ***** Main Routine Starts here *****

rps_list = ["rock", "paper", "scissors", "xxx"]
yes_no_list = ["yes", "no"]

played_before = choice_checker("Have you played before? ", yes_no_list, "Please enter y / n")
print("You chose", played_before)

user_choice = choice_checker("Choose R / P / S: ", rps_list, "Please enter R / P / S")
print("You chose", user_choice)

        