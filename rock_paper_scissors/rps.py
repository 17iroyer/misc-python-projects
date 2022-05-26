#Rock Paper Scissors in Python!
#Play a quick game of rock paper scissors against the machine

import random
import enum

#Number of total choices available, more useful when adding more complex game types
#Rock, Paper, Scissors = 3 choices
PICK_NUM = 3

class choices(enum.Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

#Gets a random play for the machine to use
def getOpponent():
    print("Opponent is choosing...")
    return random.randint(1, PICK_NUM)

#Prompt user for a choice of play
def getPlayer():
    print("Your turn. Choose an action!")
    for i in choices:
        print(i.value, "is", i.name)
    return int(input(">"))

#Check that the choice is a valid play
def getVerifyChoice(num):
    for i in choices:
        if i.value == num:
            return i.name
    
    print("Error: Could not verify choice")
    exit()

#Takes in picks as (player, machine)
def checkWinner(picks):
    switch = {
        (1, 3): True,
        (2, 1): True,
        (3, 2): True
    }
    return switch.get(picks, False)   

#Print welcome dash and get the machine's pick
print("***** Welcome to Basic RPS *****")

#Get the machines choice
machine_pick = getOpponent()

#Get the player's action and verify it
player_pick = getPlayer()
getVerifyChoice(player_pick)

#Compare and find a winner
if player_pick == machine_pick:
    print("Draw!")
elif checkWinner((player_pick, machine_pick)):
    print("You are a winner!")
else:
    print("You Lose!")

print("Your pick:", getVerifyChoice(player_pick))
print("Machine's pick", getVerifyChoice(machine_pick))