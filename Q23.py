# Card game called “Dragons 
# and Wizards”. 
# Make two teams DRAGONS and WIZARDS
# The rules for the game are as follows: 
# • If the card drawn is a diamond or a club, Team 
# DRAGONS gets a point
# • If the card drawn is a heart which is a number, 
# Team WIZARDS gets a point
# • If the card drawn is a heart that is not a number, 
# Team DRAGONS gets a point
# • For any other card, Team WIZARDS gets a point
# • The team with highest point is the winner
# Let us identify the following for a card:
# Input: shape, value
# Process: Increment in respective team scores by one 
# based on the outcome of the card drawn, as defined in 
# the rules.
# Output: Winning team

shape = str(input("Enter shape of card(diamond, club, spades, heart): "))
num = input("Enter number of card: ")
count_dragon = 0
count_wizard = 0

if shape == "diamond" or shape == "club":
    count_dragon += 1

elif shape == "heart" and num != 'A' and num != 'K' and num != 'Q' and num != 'J': 
    count_wizard += 1

elif shape == "heart" and num == 'A' and num == 'K' and num == 'Q' and num == 'J': 
    count_dragon += 1

else:
    count_wizard += 1

print("Score of Team dragon is : " + str(count_dragon))
print("Score of Team Wizard is : " + str(count_wizard))

if(count_wizard > count_dragon):
    print("Team Wizard is Winner")

else:
    print("Team Dragon is Winner")



 