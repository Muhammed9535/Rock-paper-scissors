import random
print("Welcome to Rock, Paper,Scissors!")
while True:

    game = [ "R", "P", "S"]
    computer = random.choice(game)
    player = ""
    while player not in game or player == computer:
        player = input("Enter an option [R for rock, P for Paper , S for Scissors]: ").upper()
        if player in game:
            if player == computer:
                print("player: " ,player , "computer: ", computer)
                print("There is Tie play again")
            elif player == "R":
                if computer == "P":
                    print("player: " ,player , "computer: ", computer)
                    print("player lose")
                if computer == "S":
                    print("player: " ,player , "computer: ", computer)
                    print("player Win")
            elif player == "S":
                if computer == "P":
                    print("player: " ,player , "computer: ", computer)
                    print("player Won")
                if computer == "R":
                    print("player: " ,player , "computer: ", computer)
                    print("player lose")
            elif player == "P":
                if computer == "R":
                    print("player: " ,player , "computer: ", computer)
                    print("player won")
                if computer == "S":
                    print("player: " ,player , "computer: ", computer)
                    print("player lose")
        else:
            print("invalid input,Try again!")  
    replay = input(" Do you want to replay game [Enter yes or no]: ")

    if replay != "yes":
        break

print("Byee!")                
                



    






