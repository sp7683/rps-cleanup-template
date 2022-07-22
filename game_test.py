# this is the "game_test.py" file...

#
# if you want to setup your winner determination function to return a message about who won,
# use this test:
#

from game import winner

def test_winner():
    tie_message = "It's a tie!"
    win_message = "The user wins"
    lose_message = "The computer wins"

    assert winner(u="rock", c="paper") == lose_message
    assert winner(u="rock", c="rock") == tie_message
    assert winner(u="rock", c="scissors") == win_message

    assert winner(u="paper", c="paper") == tie_message
    assert winner(u="paper", c="rock") == win_message
    assert winner(u="paper", c="scissors") == lose_message

    assert winner(u="scissors", c="paper") == win_message
    assert winner(u="scissors", c="rock") == lose_message
    assert winner(u="scissors", c="scissors") == tie_message

#
# if you want to setup your winner determination function to return the winning choice,
# use this test:
#

#from game import winning_choice
#
#def test_winning_choice():
#    assert winning_choice(u="rock", c="paper") == "paper"
#    assert winning_choice(u="rock", c="rock") == None
#    assert winning_choice(u="rock", c="scissors") == "rock"
#
#    assert winning_choice(u="paper", c="paper") == None
#    assert winning_choice(u="paper", c="rock") == "paper"
#    assert winning_choice(u="paper", c="scissors") == "scissors"
#
#    assert winning_choice(u="scissors", c="paper") == "scissors"
#    assert winning_choice(u="scissors", c="rock") == "rock"
#    assert winning_choice(u="scissors", c="scissors") == None


