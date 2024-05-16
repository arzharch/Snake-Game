import tkinter as tk
from tkinter import messagebox

# Define colors
button_colors = {
    "A* Algorithm": "#FF6F61",  # Red
    "Min Max Algorithm": "#6B5B95",  # Purple
    "Self-Playing Algorithm": "#88B04B"  # Green
}

def a_star_info():
    info = ("A* Algorithm is a popular pathfinding algorithm used in games and robotics.\n\n"
            "It finds the shortest path from a starting point to a goal while considering the cost of movement "
            "and an estimate of the remaining distance to the goal.\n\n"
            "In the context of the Snake game, A* can be used to find the best path for the snake to reach the food.")
    messagebox.showinfo("A* Algorithm", info)
    import snake_game

def min_max_info():
    info = ("Minimax Algorithm is a decision-making algorithm commonly used in two-player games.\n\n"
            "It works by considering all possible future moves and their outcomes, "
            "then choosing the move that leads to the best possible result for the current player, "
            "assuming the opponent also plays optimally.\n\n"
            "In the context of the Snake game, Minimax can be used to simulate the snake's moves "
            "and the opponent's moves (if applicable) to decide the best move to make.")
    messagebox.showinfo("Min Max Algorithm", info)
    import minmax

def self_play_info():
    info = ("Self-Playing Algorithm refers to algorithms that allow a program to play a game autonomously, "
            "often without human intervention.\n\n"
            "In the context of the Snake game, a self-playing algorithm could involve implementing an AI "
            "that controls the movements of the snake to play the game without user input.")
    messagebox.showinfo("Self-Playing Algorithm", info)
    import play_game

root = tk.Tk()
root.title("AI Mini Project")
root.geometry("200x200")
root.configure(bg="#E0E0E0")  # Light gray background

# Create a frame to contain the buttons and align it to the left
button_frame = tk.Frame(root, bg="#E0E0E0")
button_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Create buttons with custom colors
button_a_star = tk.Button(button_frame, text="A* Algorithm", command=a_star_info, bg=button_colors["A* Algorithm"], fg="white")
button_a_star.pack(fill=tk.X, pady=5)

button_min_max = tk.Button(button_frame, text="Min Max Algorithm", command=min_max_info, bg=button_colors["Min Max Algorithm"], fg="white")
button_min_max.pack(fill=tk.X, pady=5)

button_self_play = tk.Button(button_frame, text="Self-Playing Algorithm", command=self_play_info, bg=button_colors["Self-Playing Algorithm"], fg="white")
button_self_play.pack(fill=tk.X, pady=5)

root.mainloop()
