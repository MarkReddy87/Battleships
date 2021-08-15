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
        try:
            guess_row = int(input("\nPlease guess a row: "))
            print(f"You guessed row: {guess_row}")
        except ValueError:
            print("Can only enter number's, try again!")
            play_game()
        try:
            guess_col = int(input("Please guess a column: "))
            print(f"You guessed: {guess_col}")
        except ValueError:
            print("Can only enter number's, try again!")
            play_game()

        if guess_row == ship_row and guess_col == ship_col:
            print("You Win! Battleship destroyed\n")
            board[guess_row][guess_col] = "*"
            exit()
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("You missed the board, try again!")
                play_game()
            elif (board[guess_row][guess_col] == "@"):
                print("That was guessed already, please try again!")
                play_game()
            else:
                print("\nMiss! Please try again\n")
                board[guess_row][guess_col] = "@"
                print_board(board)

        comp_guess_row = randint(0, len(board) - 1)
        comp_guess_col = randint(0, len(board[0]) - 1)
        print(f"\nComputer guessed row: {comp_guess_row}")
        print(f"Computer guessed column: {comp_guess_col}")

        if comp_guess_row == ship_row and comp_guess_col == ship_col:
            print("Computer Hit! You lose battleships\n")
            board[guess_row][guess_col] = "*"
            exit()
        else:
            if (board[comp_guess_row][comp_guess_col] == "@"):
                print("Computer made a duplicate guess, your turn again")
                play_game()
            else:
                print("Computer Missed!\n")
                board[comp_guess_row][comp_guess_col] = "@"
                print_board(board)

    if guesses >= 9:
        print("You ran out of guesses, it's a draw :-( Please try again!")


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
