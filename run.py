from random import randint


def new_game():
    """
    Starts new game, sets board size and number of ships.
    Print welcome message and takes players name. 
    """
    size = 5
    num_ships = 4
    print("<","-" * 38,">")
    print(" Welcome to the classic Battleships game!")
    print(f" The game board is a {size} x {size} square")
    print(f" You and the computer have {num_ships} ships each")
    print(" The top left corner is Row:0 Col:0")
    print("<","-" * 38,">")
    player_name = input(" Please enter your name here:")
    print(f" Good luck {player_name} and remember to have fun!")
    print("<","-" * 38,">")


new_game()
