# A launcher for Rock Paper Scissor and it's variations
# Allows the user to pick the game variation they want to play

import rps

again_choice = True
game_again = True

def makeChoice(pick):
    if pick == 1:
        rps.run
    else:
        print("Invalid choice")

def getChoice():
    print("Pick a game variation to play."),
    print("1 - Basic Rock Paper Scissors")
    print("2 - Rock Paper Scissors Lizard Spock")
    return int(input("> "))

def getAgain():
    temp = int(input("> "))

    if temp == 1:
        return True
    else:
        return False

while again_choice == True:
    player_choice = getChoice()

    while game_again != True:
        makeChoice(player_choice)

        print("Play same game again? (1=yes, 0=no"),
        game_again = getAgain()
    
    print("Want to choose another game? (1=yes, 0=no)")
    again_choice = getAgain()

print("GoodBye!")
exit()