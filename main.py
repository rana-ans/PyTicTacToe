import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("PyTk Tic Tac Toe")
        self.current_player = 'X'  # Player is 'X', computer is 'O'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_score = 0
        self.computer_score = 0
        self.create_board()

    def create_board(self):
        score_label = tk.Label(self.root, text=f"You {self.player_score} - {self.computer_score} Computer")
        score_label.grid(row=3, column=1)
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'X':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
                self.reset_game()
            else:
                self.current_player = 'O'
                self.root.after(500, self.computer_move)  # Delay computer move for a better experience

    def computer_move(self):
        move = self.find_best_move()
        if move:
            row, col = move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')
            if self.check_win('O'):
                messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
                self.reset_game()
            else:
                self.current_player = 'X'

    def find_best_move(self):
        # Check if computer can win in the next move
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'O'
                    if self.check_win('O'):
                        self.board[row][col] = ' '
                        return (row, col)
                    self.board[row][col] = ' '

        # Check if player can win in the next move and block them
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X'
                    if self.check_win('X'):
                        self.board[row][col] = ' '
                        return (row, col)
                    self.board[row][col] = ' '

        # Otherwise, make a random move
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
        if empty_cells:
            return random.choice(empty_cells)
        return None

    def check_win(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                self.player_score += 1
                return True

        # Check columns
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                self.player_score += 1
                return True

        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]) or \
           all([self.board[i][2 - i] == player for i in range(3)]):
            self.player_score += 1
            return True

        self.computer_score += 1
        return False

    def check_draw(self):
        return all([cell in ['X', 'O'] for row in self.board for cell in row])

    def reset_game(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
