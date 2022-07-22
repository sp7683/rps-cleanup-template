



from random import choice

valid_options = ["rock", "paper", "scissors"]


def winner(u, c):
    if u == "rock" and c == "rock":
        return "It's a tie!"
    elif u == "rock" and c == "paper":
        return "The computer wins"
    elif u == "rock" and c == "scissors":
        return "The user wins"

    elif u == "paper" and c == "rock":
        return "The computer wins"
    elif u == "paper" and c == "paper":
        return "It's a tie!"
    elif u == "paper" and c == "scissors":
        return "The user wins"

    elif u == "scissors" and c == "rock":
        return "The computer wins"
    elif u == "scissors" and c == "paper":
        return "The user wins"
    elif u == "scissors" and c == "scissors":
        return "It's a tie!"

if __name__ == "__main__":


    #
    # USER SELECTION
    #

    choices = ["rock", "paper", "scissors"]

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(choices)
    print("COMPUTER CHOICE:", c)

    print("copy")

    #
    # DETERMINATION OF WINNER
    #

    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("The user wins")

    elif u == "paper" and c == "rock":
        print("The computer wins")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The user wins")

    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("The user wins")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")
