import tkinter as tk
import random
from config_snake import *

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.menu_frame = tk.Frame(root)
        self.level = tk.StringVar("Середній")
        self.score = 0
        self.running = False
        self.paused = False


if __name__ == "__main__":
    root = tk.Tk()
    snake = SnakeGame(root)
    root.mainloop()
