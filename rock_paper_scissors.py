player_one = input("Player one's choice: ")
player_two = input("player two's choice: ")
if player_one == "rock":
    if player_two == "rock":
        print("Tie.")
    elif player_two == "paper":
        print("Player two wins.")
    elif player_two == "scissors":
        print("Player one wins.")
    else:
        print("You did not introduce a valid play.")    
if player_one == "paper":
    if player_two == "rock":
        print("Player one wins.")
    elif player_two == "paper":
        print("Tie.")
    elif player_two == "scissors":
        print("Player two wins.")
    else:
        print("You did not introduce a valid play.")    
if player_one == "scissors":
    if player_two == "rock":
        print("Player two wins.")
    elif player_two == "paper":
        print("Player one wins.")
    elif player_two == "scissors":
        print("Tie.")
    else:
        print("You did not introduce a valid play.")