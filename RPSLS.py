<<<<<<< HEAD
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "That is not an option. Please choose again."

#Test print name_to_number("Spock")
    

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return"scissors" 
    
#Test print number_to_name(3)

def rpsls(player_choice): 
    import random
    # print a blank line to separate consecutive games
    print " "
    # print out the message for the player's choice
    print "You choose " + player_choice + "!"
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "The computer has choosen", comp_choice, "!"
    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number)%5
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print "It's a tie!"
    elif difference <=2:
        print "You win!"
    elif difference >= 3:
        print "Comptuer wins!"
    else:
        print "Something is wrong"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
