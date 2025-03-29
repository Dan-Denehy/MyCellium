import tkinter as tk
from core.cell import Cell
from config.settings import HEADER_BG_COLOR, HEADER_TEXT_COLOR, CELL_FONT, HEADER_FONT, CELL_WIDTH

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
        # Create column headers (A, B, C, ...)
        for col in range(self.cols):
            header = tk.Entry(
                self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                font=HEADER_FONT, readonlybackground=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR
            )
            header.insert(0, chr(65 + col))  # A, B, C, ...
            header.config(state="readonly")
            header.grid(row=0, column=col + 1, padx=1, pady=1)

        # Create row headers (1, 2, 3, ...)
        for row in range(self.rows):
            header = tk.Entry(
                self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                font=HEADER_FONT, readonlybackground=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR
            )
            header.insert(0, str(row + 1))  # 1, 2, 3, ...
            header.config(state="readonly")
            header.grid(row=row + 1, column=0, padx=1, pady=1)

        # Create grid cells
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                entry = tk.Entry(
                    self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                    font=CELL_FONT
                )
                entry.grid(row=row + 1, column=col + 1, padx=1, pady=1)
                entry.insert(0, cell.get_value())

                # Bind events for editing and saving cell values
                entry.bind("<Return>", lambda e, r=row, c=col, ent=entry: self.update_cell(r, c, ent.get()))
                entry.bind("<FocusOut>", lambda e, r=row, c=col, ent=entry: self.update_cell(r, c, ent.get()))

    def update_cell(self, row, col, value):
        self.cells[row][col].set_value(value)
        print(f"Updated Cell({row}, {col}) to '{value}'")
