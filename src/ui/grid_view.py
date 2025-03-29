import tkinter as tk
from core.cell import Cell


class GridView:
    def __init__(self, root, rows=10, cols=10):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]

        # Create a frame to hold the grid
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        self.create_grid()

    def create_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                entry = tk.Entry(self.frame, width=10, justify="center")
                entry.grid(row=row, column=col, padx=1, pady=1)
                entry.insert(0, cell.get_value())

                # Properly capture the current row, col, and entry
                entry.bind("<FocusOut>", lambda e, r=row, c=col, ent=entry: self.update_cell(r, c, ent.get()))

    def update_cell(self, row, col, value):
        self.cells[row][col].set_value(value)
        print(f"Updated Cell({row}, {col}) to '{value}'")
