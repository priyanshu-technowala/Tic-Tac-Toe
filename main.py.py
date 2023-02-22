def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    # Check rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    # Check columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    # No win
    return False

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "P"
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        move = int(input("Enter move (1-9): ")) - 1
        if board[move] != " ":
            print("That spot is already taken.")
            continue
        board[move] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break
        current_player = "O" if current_player == "P" else "P"

play_game()
