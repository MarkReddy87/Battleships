from random import randint

"""
Defining variables
"""
size = 5
player_guesses = 10
board = []

"""
Creating battleship board
"""


for i in range(0, 5):
    board.append(["#"]*5)


def print_board(board):
    for row in board:
        print(" ".join(row))


"""
choosing random row and column for ship on board and
storing it in a variable
"""


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


def play_game():
    for guesses in range(10):
        guess_row = input("\nPlease guess a row: ")
        guess_col = input("Please guess a column: ")
        print(f"\nYou guessed row:{guess_row} and column:{guess_col}")

        if guess_row == ship_row and guess_col == ship_col:
            print("Hit! You sunk my battleship\n")
            break
        else:
            print("Miss! Please try again\n")

        comp_guess_row = randint(0, len(board) - 1)
        comp_guess_col = randint(0, len(board[0]) - 1)
        print(f"Computer guessed row:{comp_guess_row} and cloumn:{comp_guess_col}")

        if comp_guess_row == ship_row and comp_guess_col == ship_col:
            print("Computer Hit! You lose battleships\n")
            break
        else:
            print("Computer Missed!")

    if guesses >= 9:
        print("You ran out of guesses :-() Please try again!")


def new_game():
    """
    Starts game, prints welcome message, takes players name and runs
    play_game function.
    """
    print("<", "-" * 38, ">")
    print(" Welcome to the classic Battleships game!")
    print(f" The game board is a {size} x {size} square")
    print(" The top left corner is Row:0 Col:0")
    print(f" You have {player_guesses} guesses")
    print("<", "-" * 38, ">")
    player_name = input(" Please enter your name here:")
    print(f" Good luck {player_name} and remember to have fun!")
    print("<", "-" * 38, ">\n")

    print("Battleship Board:\n")
    print_board(board)

    play_game()


new_game()
