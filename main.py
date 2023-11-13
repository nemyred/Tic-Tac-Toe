# Create the board
board = [' ' for _ in range(9)]
current = []
end = False


# Function to print the board
def print_board():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')


def check_draw():
    if ' ' not in board:
        return True
    return False


# Function to check for a win
def check_win(player):

    # Rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    # Columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    # Diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


# Function to play the game
def play_game():
    current_player = ""
    game_over = False
    while not game_over:
        print_board()
        if not current:
            choice = input("Choose a character between X and O: ").upper()
            current.append(choice)
            current_player = choice[-1]
        elif current[-1] == "X":
            current_player = "O"
            current.append(current_player)
        elif current[-1] == "O":
            current_player = "X"
            current.append(current_player)

        # Get player's move
        move = input(f"It's  {current_player}'s turn. Enter a position (1-9): ")

        # Validate and update the board
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            board[int(move) - 1] = current_player
            print_board()
        else:
            print("Invalid move. Try again.")
            continue

        # Check for a win
        if check_win(current_player):
            print_board()
            print(current_player + " wins!")
            game_over = True
            # Check for a draw
        elif check_draw():
            print_board()
            print("It's a draw!")
            game_over = True


play_game()
