
import random as r

player = "X"
winner = None
gamerunning = True

print("--------- TIC TAC TOE ---------\n")

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def player_input(board):
    global player

    pos = int(input("Enter a number between 1-9: "))

    if 1 <= pos <= 9 and board[pos - 1] == "-":
        board[pos - 1] = player
    else:
        print("Invalid move!")


# Check rows
def check_rows(board):
    global winner

    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True

    return False


# Check columns
def check_columns(board):
    global winner

    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True

    return False


# Check diagonals
def check_diagonals(board):
    global winner

    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True

    return False


# Check if anyone has won
def check_win(board):
    return (
        check_rows(board)
        or check_columns(board)
        or check_diagonals(board)
    )

# adding computer

print_board(board)

while gamerunning:
    player_input(board)
    print_board(board)

    if check_win(board):
        print(f"{winner} wins!")
        gamerunning = False