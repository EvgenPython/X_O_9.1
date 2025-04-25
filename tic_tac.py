import random
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.comp = "O"
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_game(self.player):
                messagebox.showinfo("Гра закінчена", "Ти переміг!")
            elif "" not in self.board:
                messagebox.showinfo("Гра закінчена", "Нічия!!")
                self.reset_game()
            else:
                self.root.after(500, self.comp_move)

    def comp_move(self):
        empty_indexes = [i for i, val in enumerate(self.board) if val == ""]
        if not empty_indexes:
            return
        move = random.choice(empty_indexes)
        self.board[move] = self.comp
        self.buttons[move].config(text=self.comp)
        if self.check_game(self.comp):
            messagebox.showinfo("Гра закінчена", "Комп переміг!")
        elif "" not in self.board:
            messagebox.showinfo("Гра закінчена", "Нічия!!")
            self.reset_game()

    def check_game(self, symbol):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 5, 8), (2, 5, 6)
        ]
        for a,b,c in combos:
            if self.board[a] == self.board[b] == self.board[c] == symbol:
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
