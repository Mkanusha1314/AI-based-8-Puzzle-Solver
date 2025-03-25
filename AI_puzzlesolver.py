import tkinter as tk
from tkinter import messagebox
import time
from collections import deque

class PuzzleSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Solver")
        self.tiles = []
        self.board_values = []

        # Set up GUI Layout
        self.setup_gui()

    def setup_gui(self):
        # Heading
        heading = tk.Label(self.root, text="Puzzle Solver", font=("Arial", 18), pady=10)
        heading.grid(row=0, column=0, columnspan=4)

        # Initial Value Entry
        self.initial_value_label = tk.Label(self.root, text="Initial Value (comma-separated):")
        self.initial_value_label.grid(row=1, column=0, columnspan=2)

        self.initial_value_entry = tk.Entry(self.root, width=30)
        self.initial_value_entry.grid(row=1, column=2, columnspan=2)

        self.submit_button = tk.Button(self.root, text="Set Puzzle", command=self.set_puzzle)
        self.submit_button.grid(row=2, column=0, columnspan=4)

        # Puzzle Tiles (inside a big square)
        puzzle_frame = tk.Frame(self.root, relief="solid", bd=5)
        puzzle_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        for row in range(3):
            row_tiles = []
            for col in range(3):
                tile = tk.Label(puzzle_frame, text="", font=("Arial", 24), width=5, height=3,
                                relief="solid", borderwidth=0, bg="lightblue")
                tile.grid(row=row, column=col, padx=0, pady=0)  # Set padx and pady to 0 for no gaps
                row_tiles.append(tile)
            self.tiles.append(row_tiles)

        # BFS / DFS Options
        self.algo_choice_label = tk.Label(self.root, text="Select Algorithm:")
        self.algo_choice_label.grid(row=4, column=0, columnspan=2)

        self.algo_var = tk.StringVar(value="bfs")
        self.bfs_button = tk.Radiobutton(self.root, text="BFS", variable=self.algo_var, value="bfs")
        self.dfs_button = tk.Radiobutton(self.root, text="DFS", variable=self.algo_var, value="dfs")
        self.bfs_button.grid(row=4, column=2)
        self.dfs_button.grid(row=4, column=3)

        # Solve Button
        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        self.solve_button.grid(row=5, column=0, columnspan=4, pady=10)

        # Result Labels
        self.result_labels = {
            'cost_of_path': tk.Label(self.root, text="Cost of Path: N/A"),
            'nodes_expanded': tk.Label(self.root, text="Nodes Expanded: N/A"),
            'search_depth': tk.Label(self.root, text="Search Depth: N/A"),
            'max_search_depth': tk.Label(self.root, text="Max Search Depth: N/A"),
            'running_time': tk.Label(self.root, text="Running Time: N/A")
        }

        for i, label in enumerate(self.result_labels.values()):
            label.grid(row=6 + i, column=0, columnspan=4)

    def set_puzzle(self):
        # Get initial values from the entry
        initial_values = self.initial_value_entry.get().split(",")
        if len(initial_values) != 9:
            messagebox.showerror("Error", "Please enter exactly 9 comma-separated values.")
            return

        try:
            initial_values = [int(i) for i in initial_values]
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers.")
            return

        # Set the values on the tiles
        for row in range(3):
            for col in range(3):
                value = initial_values[row * 3 + col]
                self.tiles[row][col].config(text=str(value) if value != 0 else "")

        self.board_values = initial_values

    def solve_puzzle(self):
        if not self.board_values:
            messagebox.showerror("Error", "Please set the puzzle values first.")
            return

        # Reset the result values to N/A before solving again
        for label in self.result_labels.values():
            label.config(text="N/A")

        algorithm = self.algo_var.get()
        start_time = time.time()

        if algorithm == "bfs":
            cost_of_path, nodes_expanded, search_depth, max_search_depth = self.bfs(self.board_values)
        else:
            cost_of_path, nodes_expanded, search_depth, max_search_depth = self.dfs(self.board_values)

        end_time = time.time()
        running_time = end_time - start_time

        # Update result labels with actual calculated values
        self.result_labels['running_time'].config(text=f"Running Time: {running_time:.8f}")
        self.result_labels['cost_of_path'].config(text=f"Cost of Path: {cost_of_path}")
        self.result_labels['nodes_expanded'].config(text=f"Nodes Expanded: {nodes_expanded}")
        self.result_labels['search_depth'].config(text=f"Search Depth: {search_depth}")
        self.result_labels['max_search_depth'].config(text=f"Max Search Depth: {max_search_depth}")

        # Update the puzzle state to goal (for demonstration)
        goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for row in range(3):
            for col in range(3):
                value = goal_state[row * 3 + col]
                self.tiles[row][col].config(text=str(value) if value != 0 else "")

    def bfs(self, start_state):
        # BFS algorithm logic
        nodes_expanded = 0
        search_depth = 0
        max_search_depth = 0
        cost_of_path = 0

        goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        start_state_tuple = tuple(start_state)
        queue = deque([(start_state_tuple, [], 0)])  # (state, path, depth)
        visited = set()

        while queue:
            state, path, depth = queue.popleft()
            nodes_expanded += 1

            if state == goal_state:
                cost_of_path = len(path)
                search_depth = depth
                max_search_depth = max(max_search_depth, depth)
                break

            for move in self.generate_moves(state):
                new_state = self.make_move(state, move)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state], depth + 1))
                    max_search_depth = max(max_search_depth, depth + 1)

        return cost_of_path, nodes_expanded, search_depth, max_search_depth

    def dfs(self, start_state):
        # DFS algorithm logic
        nodes_expanded = 0
        search_depth = 0
        max_search_depth = 0
        cost_of_path = 0

        goal_state


import tkinter as tk
from tkinter import messagebox
import time
from collections import deque


class PuzzleSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Solver")
        self.tiles = []
        self.board_values = []

        # Set up GUI Layout
        self.setup_gui()

    def setup_gui(self):
        # Heading
        heading = tk.Label(self.root, text="Puzzle Solver", font=("Arial", 18), pady=10)
        heading.grid(row=0, column=0, columnspan=4)

        # Initial Value Entry
        self.initial_value_label = tk.Label(self.root, text="Initial Value (comma-separated):")
        self.initial_value_label.grid(row=1, column=0, columnspan=2)

        self.initial_value_entry = tk.Entry(self.root, width=30)
        self.initial_value_entry.grid(row=1, column=2, columnspan=2)

        self.submit_button = tk.Button(self.root, text="Set Puzzle", command=self.set_puzzle)
        self.submit_button.grid(row=2, column=0, columnspan=4)

        # Puzzle Tiles (inside a big square)
        puzzle_frame = tk.Frame(self.root, relief="solid", bd=5)
        puzzle_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        for row in range(3):
            row_tiles = []
            for col in range(3):
                tile = tk.Label(puzzle_frame, text="", font=("Arial", 24), width=4, height=2, relief="ridge",
                                borderwidth=2)
                tile.grid(row=row, column=col, padx=5, pady=5)
                row_tiles.append(tile)
            self.tiles.append(row_tiles)

        # BFS / DFS Options
        self.algo_choice_label = tk.Label(self.root, text="Select Algorithm:")
        self.algo_choice_label.grid(row=4, column=0, columnspan=2)

        self.algo_var = tk.StringVar(value="bfs")
        self.bfs_button = tk.Radiobutton(self.root, text="BFS", variable=self.algo_var, value="bfs")
        self.dfs_button = tk.Radiobutton(self.root, text="DFS", variable=self.algo_var, value="dfs")
        self.bfs_button.grid(row=4, column=2)
        self.dfs_button.grid(row=4, column=3)

        # Solve Button
        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        self.solve_button.grid(row=5, column=0, columnspan=4, pady=10)

        # Result Labels
        self.result_labels = {
            'cost_of_path': tk.Label(self.root, text="Cost of Path: N/A"),
            'nodes_expanded': tk.Label(self.root, text="Nodes Expanded: N/A"),
            'search_depth': tk.Label(self.root, text="Search Depth: N/A"),
            'max_search_depth': tk.Label(self.root, text="Max Search Depth: N/A"),
            'running_time': tk.Label(self.root, text="Running Time: N/A")
        }

        for i, label in enumerate(self.result_labels.values()):
            label.grid(row=6 + i, column=0, columnspan=4)

    def set_puzzle(self):
        # Get initial values from the entry
        initial_values = self.initial_value_entry.get().split(",")
        if len(initial_values) != 9:
            messagebox.showerror("Error", "Please enter exactly 9 comma-separated values.")
            return

        try:
            initial_values = [int(i) for i in initial_values]
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers.")
            return

        # Set the values on the tiles
        for row in range(3):
            for col in range(3):
                value = initial_values[row * 3 + col]
                self.tiles[row][col].config(text=str(value) if value != 0 else "")

        self.board_values = initial_values

    def solve_puzzle(self):
        if not self.board_values:
            messagebox.showerror("Error", "Please set the puzzle values first.")
            return

        # Reset the result values to N/A before solving again
        for label in self.result_labels.values():
            label.config(text="N/A")

        algorithm = self.algo_var.get()
        start_time = time.time()

        if algorithm == "bfs":
            cost_of_path, nodes_expanded, search_depth, max_search_depth = self.bfs(self.board_values)
        else:
            cost_of_path, nodes_expanded, search_depth, max_search_depth = self.dfs(self.board_values)

        end_time = time.time()
        running_time = end_time - start_time

        # Update result labels with actual calculated values
        self.result_labels['running_time'].config(text=f"Running Time: {running_time:.8f}")
        self.result_labels['cost_of_path'].config(text=f"Cost of Path: {cost_of_path}")
        self.result_labels['nodes_expanded'].config(text=f"Nodes Expanded: {nodes_expanded}")
        self.result_labels['search_depth'].config(text=f"Search Depth: {search_depth}")
        self.result_labels['max_search_depth'].config(text=f"Max Search Depth: {max_search_depth}")

        # Update the puzzle state to goal (for demonstration)
        goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for row in range(3):
            for col in range(3):
                value = goal_state[row * 3 + col]
                self.tiles[row][col].config(text=str(value) if value != 0 else "")

    def bfs(self, start_state):
        nodes_expanded = 0
        search_depth = 0
        max_search_depth = 0
        cost_of_path = 0

        goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        start_state_tuple = tuple(start_state)
        queue = deque([(start_state_tuple, [], 0)])  # (state, path, depth)
        visited = set()

        while queue:
            state, path, depth = queue.popleft()
            nodes_expanded += 1

            if state == goal_state:
                cost_of_path = len(path)
                search_depth = depth
                max_search_depth = max(max_search_depth, depth)
                break

            # Generate possible moves
            for move in self.possible_moves(state):
                new_state = self.make_move(state, move)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state], depth + 1))
                    max_search_depth = max(max_search_depth, depth + 1)

        return cost_of_path, nodes_expanded, search_depth, max_search_depth

    def dfs(self, start_state):
        nodes_expanded = 0
        search_depth = 0
        max_search_depth = 0
        cost_of_path = 0

        goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
        start_state_tuple = tuple(start_state)
        stack = [(start_state_tuple, [], 0)]  # (state, path, depth)
        visited = set()

        while stack:
            state, path, depth = stack.pop()
            nodes_expanded += 1

            if state == goal_state:
                cost_of_path = len(path)
                search_depth = depth
                max_search_depth = max(max_search_depth, depth)
                break

            # Generate possible moves
            for move in self.possible_moves(state):
                new_state = self.make_move(state, move)
                if new_state not in visited:
                    visited.add(new_state)
                    stack.append((new_state, path + [new_state], depth + 1))
                    max_search_depth = max(max_search_depth, depth + 1)

        return cost_of_path, nodes_expanded, search_depth, max_search_depth

    def make_move(self, state, move):
        state = list(state)
        zero_index = state.index(0)

        if move == 'up' and zero_index >= 3:
            state[zero_index], state[zero_index - 3] = state[zero_index - 3], state[zero_index]
        elif move == 'down' and zero_index <= 5:
            state[zero_index], state[zero_index + 3] = state[zero_index + 3], state[zero_index]
        elif move == 'left' and zero_index % 3 != 0:
            state[zero_index], state[zero_index - 1] = state[zero_index - 1], state[zero_index]
        elif move == 'right' and zero_index % 3 != 2:
            state[zero_index], state[zero_index + 1] = state[zero_index + 1], state[zero_index]

        return tuple(state)

    def possible_moves(self, state):
        zero_index = state.index(0)
        moves = []

        if zero_index >= 3:  # Can move up
            moves.append('up')
        if zero_index <= 5:  # Can move down
            moves.append('down')
        if zero_index % 3 != 0:  # Can move left
            moves.append('left')
        if zero_index % 3 != 2:  # Can move right
            moves.append('right')

        return moves


if __name__ == "__main__":
    root = tk.Tk()
    puzzle_gui = PuzzleSolverGUI(root)
    root.mainloop()
