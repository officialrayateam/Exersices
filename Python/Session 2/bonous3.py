player1 = input("Enter r,p,s :")
player2 = input("Enter r,p,s :")

if player1 == player2:
    print("Draw")

elif player1 == "r":
    if player2 == "p":
        print("Player 2 Wins.")
    elif player2 == "s":
        print("Player 1 Wins.")

elif player1 == "p":
    if player2 == "r":
        print("Player 1 Wins.")
    elif player2 == "s":
        print("Player 2 Wins.")

elif player1 == "s":
    if player2 == "r":
        print("Player 2 Wins.")
    elif player2 == "p":
        print("Player 1 Wins.")
else:
    print("Error.")

###################################################
statuses = {
    "r,r": "draw",
    "r,s": "player 1 wins",
    "r,p": "player 2 wins",
    "p,p": "draw",
    "p,r": "player 1 wins",
    "p,s": "player 2 wins",
    "s,s": "draw",
    "s,p": "player 1 wins",
    "s,r": "player 2 wins",
}

print(statuses[f"{player1},{player2}"])
