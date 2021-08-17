from random import randint

"""
Defining variables
"""
size = 5
guesses = 5
board = []
turns = 0
guess_row = ""
guess_col = ""

"""
Initializes playing board
"""
for i in range(0, 5):
    board.append(["#"]*5)


def print_board(board):
    """
    Print's battleship board
    """
    for row in board:
        print(" ".join(row))


def random_row(board):
    """
    choosing random row for ship on board
    """
    return randint(0, len(board) - 1)


def random_col(board):
    """
    choosing random column for ship on board
    """
    return randint(0, len(board[0]) - 1)


"""
Storing the ship row and column in variables
"""
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
    check_turns()
    comp_guess_row = randint(0, len(board) - 1)
    comp_guess_col = randint(0, len(board[0]) - 1)
    print(f"\nComputer guessed row: {comp_guess_row}")
    print(f"Computer guessed column: {comp_guess_col}")

    if comp_guess_row == ship_row and comp_guess_col == ship_col:
        print("Hit! You lose, computer destroyed the battleship :-( Better \
            luck next time.")
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
    """
    #Check if max guesses have been made and exit game
    """
    global turns
    if turns > 4:
        print("Sorry you ran out of guesses, better luck next time :-/")
        exit()


def check_row():
    global guess_row
    try:
        int(guess_row)
    except ValueError:
        print("Can only enter number's, try again!")
        player_guess()


def check_col():
    global guess_col
    try:
        int(guess_col)
    except ValueError:
        print("Can only enter number's, try again!")
        player_guess()


def player_guess():
    global turns
    global guess_row
    global guess_col
    check_turns()
    guess_row = input("\nPlease guess a row:\n")
    check_row()
    guess_col = input("Please guess a column:\n")
    check_col()

    if guess_row == ship_row and guess_col == ship_col:
        print("You Win! Battleship destroyed!!!!")
        board[int(guess_row)][int(guess_col)] = "*"
        print_board(board)
        exit()
    else:
        if int(guess_row) < 0 or int(guess_row) > 4 or \
                int(guess_col) < 0 or int(guess_col) > 4:
            print("You missed the board and lose a turn :-(")
            turns += 1
            comp_guess()
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
    play_game function.
    """
    check_name()
    print("<", "-" * 38, ">\n")
    print("Battleship Board:\n")
    print_board(board)

    player_guess()


def main():
    """
    Starts program, gives welcome message, tells player board size and amount
    of guesses to win
    """
    print("<", "-" * 38, ">")
    print(" Welcome to the you sunk my Battleship game!")
    print(f" The game board is a {size} x {size} square")
    print(" The top left corner is Row:0 Col:0")
    print(f" You have {guesses} guesses to win")
    print("<", "-" * 38, ">")

    new_game()


main()
