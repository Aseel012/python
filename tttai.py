import random as r

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
    pos = int(input("Enter a number between 1-9: "))

    if 1 <= pos <= 9 and board[pos - 1] == "-":
        board[pos - 1] = "X"  # You are always X
    else:
        print("Invalid move!")


def computer_input(board):
    # Get all empty positions
    empty_positions = [i for i in range(9) if board[i] == "-"]
    
    if empty_positions:
        # Choose a random empty position
        pos = r.choice(empty_positions)
        board[pos] = "O"  # Computer is always O
        print(f"Computer chose position {pos + 1}")




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



def check_tie(board):
    if "-" not in board:
        print("It's a tie!")
        return True
    return False


# Main game loop
print_board(board)

while gamerunning:
    # Your turn (X)
    player_input(board)
    print_board(board)
    
    if check_win(board):
        print(f"{winner} wins!")
        gamerunning = False
        break
    
    if check_tie(board):
        gamerunning = False
        break
    
    # Computer's turn (O)
    computer_input(board)
    print_board(board)
    
    if check_win(board):
        print(f"{winner} wins!")
        gamerunning = False
        break
    
    if check_tie(board):
        gamerunning = False
        break
