from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
 
while player == False:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Thats a Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("no, no..thats not what i asked. Choose from either rock, paper or scissors")
    
    player = False
    computer = t[randint(0,2)]
print('you win')
