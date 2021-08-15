from random import randint

"""
Creating player and computer boards
"""
computer_board = []
player_board = []

for i in range(0, 5):
    computer_board.append(["#"]*5)
for i in range(0, 5):
    player_board.append(["#"]*5)


def print_player_board(player_board):
    for row in player_board:
        print(" ".join(row))


def print_computer_board(computer_board):
    for row in computer_board:
        print(" ".join(row))


"""
choosing random row's and column's for ships on both boards and
storing them in variables
"""


def comp_random_row(computer_board):
    return randint(0, len(computer_board) - 1)


def comp_random_col(computer_board):
    return randint(0, len(computer_board[0]) - 1)


def player_random_row(player_board):
    return randint(0, len(computer_board) - 1)


def player_random_col(player_board):
    return randint(0, len(computer_board[0]) - 1)


comp_ship_row = comp_random_row(computer_board)
comp_ship_col = comp_random_col(computer_board)
player_ship_row = player_random_row(player_board)
player_ship_col = player_random_col(player_board)


def make_guess():
    guess_row = input("\nPlease guess a row: ")
    guess_col = input("Please guess a column: ")
    print(f"\nYou have guessed row:{guess_row} and column:{guess_col}")
    comp_guess_row = randint(0, len(computer_board) - 1)
    comp_guess_col = randint(0, len(computer_board[0]) - 1)
    print(f"Computer has guessed row:{comp_guess_row} and cloumn:{comp_guess_col}")


def new_game():
    """
    Starts game, sets board size and number of ships.
    Print welcome message and takes players name.
    """
    size = 5
    num_ships = 4
    print("<", "-" * 38, ">")
    print(" Welcome to the classic Battleships game!")
    print(f" The game board is a {size} x {size} square")
    print(f" You and the computer have {num_ships} ships each")
    print(" The top left corner is Row:0 Col:0")
    print("<", "-" * 38, ">")
    player_name = input(" Please enter your name here:")
    print(f" Good luck {player_name} and remember to have fun!")
    print("<", "-" * 38, ">\n")

    print(f"{player_name}'s Board:\n")
    print_player_board(player_board)
    print("\nComputer's Board:\n")
    print_computer_board(computer_board)

    make_guess()


new_game()
