from random import randint
"""
Defining variables
"""
size = 5
player_guesses = 5
board = []


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
        main()
    else:
        print(f"Welcome {player_name} and good luck")


def play_game():
    for guesses in range(5):
        try:
            guess_row = int(input("\nPlease guess a row:\n"))
            print(f"You guessed row: {guess_row}")
        except ValueError:
            print("Can only enter number's, try again!")
            play_game()
        try:
            guess_col = int(input("Please guess a column:\n"))
            print(f"You guessed: {guess_col}")
        except ValueError:
            print("Can only enter number's, try again!")
            play_game()

        if guess_row == ship_row and guess_col == ship_col:
            print("You Win! Battleship destroyed\n")
            board[guess_row][guess_col] = "*"
            exit()
        else:
            if (guess_row < 0 or guess_row > 4) or \
                    (guess_col < 0 or guess_col > 4):
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
            print("Hit! You lose, computer destroyed the battleship\n")
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

    if guesses >= 4:
        print("You ran out of guesses, it's a draw :-( Please try again!")


def new_game():
    """
    Starts new game then checks players name, prints first board and runs
    play_game function.
    """
    check_name()
    print("<", "-" * 38, ">\n")
    print("Battleship Board:\n")
    print_board(board)

    play_game()


def main():
    """
    Starts program, gives welcome message, tells player board size and amount
    of guesses to win
    """
    print("<", "-" * 38, ">")
    print(" Welcome to the you sunk my Battleship game!")
    print(f" The game board is a {size} x {size} square")
    print(" The top left corner is Row:0 Col:0")
    print(f" You have {player_guesses} guesses to win")
    print("<", "-" * 38, ">")

    new_game()


main()
