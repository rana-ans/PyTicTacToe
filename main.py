def print_board(board):
    """Function to print the current state of the board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    """Function to check if the current player has won"""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    """Function to check if the game is a draw"""
    return all([cell in ['X', 'O'] for row in board for cell in row])

def player_move(board, player):
    """Function to handle player moves"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Cell already taken. Choose another one.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the game"""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
