from random import randint

"""Defining variables"""
# creates empty board list to create playing board
board = []
# sets initial turns to 0, incremented with turns += 1
turns = 0
# sets guess_row to empty string which will be changed by input()
guess_row = ""
# sets guess_col to empty string which will be changed by input()
guess_col = ""

"""Initializes playing board"""
for _ in range(0, 5):
    board.append(["#"]*5)


def print_board(board):
    """Print's battleship board"""
    for row in board:
        print(" ".join(row))


def random_row(board):
    """choosing random row for ship on board"""
    return randint(0, len(board) - 1)


def random_col(board):
    """choosing random column for ship on board"""
    return randint(0, len(board[0]) - 1)


"""Storing the ship row and column in variables"""
ship_row = random_row(board)
ship_col = random_col(board)


def check_name():
    """
    Takes user names and checks if it is valid (cannot be blank, a number and
    must start with a letter) then prints a welcome message
    """
    player_name = input("Enter your name here:\n")
    if len(player_name) < 1 or not player_name.isalnum() or not \
            player_name[0].isalpha():
        print("Please enter a valid name")
        check_name()
    else:
        print(f"Welcome {player_name} and good luck!")


def comp_guess():
    """Generates computer guess, prints and updates the board accordingly"""
    check_turns()
    comp_guess_row = randint(0, len(board) - 1)
    comp_guess_col = randint(0, len(board[0]) - 1)
    print(f"\nComputer guessed row: {comp_guess_row}")
    print(f"Computer guessed column: {comp_guess_col}")

    if comp_guess_row == ship_row and comp_guess_col == ship_col:
        print("Hit! Computer destroyed the battleship. Better luck next time.")
        board[comp_guess_row][comp_guess_col] = "*"
        print_board(board)
        exit()
    else:
        if (board[comp_guess_row][comp_guess_col] == "@"):
            print("Computer made a duplicate guess, your turn")
            player_guess()
        else:
            print("Computer Missed!\n")
            board[comp_guess_row][comp_guess_col] = "@"
            print_board(board)
            player_guess()


def check_turns():
    """Check if max guesses have been made and exit game"""
    global turns
    if turns > 4:
        print("Sorry you ran out of guesses, better luck next time :-/")
        exit()


def check_row():
    global turns
    """Checks if row entered is a number"""
    try:
        int(guess_row)
    except ValueError:
        print("Can only enter number's form 0 - 4, try again!")
        turns += 1
        player_guess()


def check_col():
    global turns
    """Check if column entered is a number"""
    try:
        int(guess_col)
    except ValueError:
        print("Can only enter number's form 0 - 4, try again!")
        turns += 1
        player_guess()


def play_again():
    start_again = input("Want to play again? type 'y':")
    if start_again == "y" or "Y":
        main()
    else:
        exit()


def player_guess():
    """
    Takes user input, validates guesses, update turn count and checks if
    player has won.
    """
    global turns
    global guess_row
    global guess_col
    check_turns()
    guess_row = input("\nPlease guess a row:\n")
    check_row()
    if int(guess_row) < 0 or int(guess_row) > 4:
        print("You missed the board and lose a turn (only use 0 - 4)")
        turns += 1
        comp_guess()
    guess_col = input("Please guess a column:\n")
    check_col()
    if int(guess_col) < 0 or int(guess_col) > 4:
        print("You missed the board and lose a turn (only use 0 - 4)")
        turns += 1
        comp_guess()

    if guess_row == ship_row and guess_col == ship_col:
        print("You Win! Battleship destroyed!!!!")
        board[int(guess_row)][int(guess_col)] = "*"
        print_board(board)
        exit()
    elif (board[int(guess_row)][int(guess_col)] == "@"):
        print("That was guessed already, you lose a turn!")
        turns += 1
        comp_guess()
    else:
        print("\nMiss! Please try again\n")
        board[int(guess_row)][int(guess_col)] = "@"
        turns += 1
        print_board(board)
        comp_guess()


def new_game():
    """
    Starts new game then checks players name, prints first board and runs
    player_guess function.
    """
    check_name()
    print("<", "-" * 34, ">\n")
    print("Battleship Board:\n")
    print_board(board)

    player_guess()


def main():
    """
    Starts program, gives welcome message, tells player board size and amount
    of guesses they have to win
    """
    size = 5
    guesses = 5
    print("<", "-" * 34, ">")
    print(" Welcome to You Sunk My Battleship!")
    print(f" The game board is a {size} x {size} square")
    print(" The top left corner is Row:0 Col:0")
    print(f" You have {guesses} guesses to win")
    print("<", "-" * 34, ">")

    new_game()


main()
