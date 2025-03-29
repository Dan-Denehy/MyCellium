import tkinter as tk
from core.cell import Cell
from config.settings import HEADER_BG_COLOR, HEADER_TEXT_COLOR, CELL_FONT, HEADER_FONT, CELL_WIDTH

class GridView:
    def __init__(self, root, rows=10, cols=10):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.active_entry = None  # Track the currently active cell

        # Create a frame to hold the grid
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")
        self.root.bind("<Escape>", lambda event: root.focus())


        self.create_grid()

    def create_grid(self):
        # Create column headers (A, B, C, ...)
        for col in range(self.cols):
            header = tk.Entry(
                self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                font=HEADER_FONT, readonlybackground=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR
            )
            header.insert(0, chr(65 + col))
            header.config(state="readonly")
            header.grid(row=0, column=col + 1, padx=0, pady=0, sticky="nsew")

        # Create row headers (1, 2, 3, ...)
        for row in range(self.rows):
            header = tk.Entry(
                self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                font=HEADER_FONT, readonlybackground=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR
            )
            header.insert(0, str(row + 1))
            header.config(state="readonly")
            header.grid(row=row + 1, column=0, padx=0, pady=0, sticky="nsew")

        # Create grid cells (editable)
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                entry = tk.Entry(
                    self.frame, width=CELL_WIDTH, justify="center", relief="ridge", font=CELL_FONT,
                    borderwidth=1
                )
                entry.grid(row=row + 1, column=col + 1, padx=0, pady=0, sticky="nsew")
                entry.insert(0, cell.get_value())
                entry.bind("<FocusIn>", lambda e, r=row, c=col: self.set_active_entry(r, c))
                entry.bind("<Return>", lambda e, r=row, c=col, ent=entry: self.update_cell(r, c, ent.get()))
                entry.bind("<FocusOut>", lambda e, r=row, c=col: self.stop_editing(e, r, c))  # Fixed focus out event

                # Arrow key navigation
                entry.bind("<Up>", lambda e, r=row, c=col: self.navigate(r - 1, c))
                entry.bind("<Down>", lambda e, r=row, c=col: self.navigate(r + 1, c))
                entry.bind("<Left>", lambda e, r=row, c=col: self.navigate(r, c - 1))
                entry.bind("<Right>", lambda e, r=row, c=col: self.navigate(r, c + 1))
                entry.bind("<Shift-Return>", lambda e, r=row, c=col: self.navigate(r - 1, c))  # Move up on Shift+Enter
                entry.bind("<Return>", lambda e, r=row, c=col: self.navigate(r + 1, c))  # Move down on Enter



    def set_active_entry(self, row, col):
        self.active_entry = (row, col)



    def stop_editing(self, event, row=None, col=None):
        """Stop editing the active cell when clicking outside or switching cells."""

        print(f"row={row}, col={col}")

        if row is not None and col is not None:
            # Log invalid row or column if None is passed
            if self.active_entry is not None:
                print("closing edit and saving")
                self.update_cell(self.active_entry[0], self.active_entry[1],self.frame.grid_slaves(row=self.active_entry[0] + 1, column=self.active_entry[1] + 1)[0].get())




    def navigate(self, row, col):
        """Move focus to the specified cell if within bounds."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            entry_widget = self.frame.grid_slaves(row=row + 1, column=col + 1)
            if entry_widget:
                entry_widget[0].focus_set()

    def update_cell(self, row, col, value):
        self.cells[row][col].set_value(value)
        print(f"Updated Cell({row}, {col}) to '{value}'")
