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

        # Bind click outside of cells to stop editing
        self.root.bind("<Button-1>", self.stop_editing)

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
            header.grid(row=0, column=col + 1, padx=1, pady=1)

        # Create row headers (1, 2, 3, ...)
        for row in range(self.rows):
            header = tk.Entry(
                self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                font=HEADER_FONT, readonlybackground=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR
            )
            header.insert(0, str(row + 1))
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

                # Bind focus and key events
                entry.bind("<FocusIn>", lambda e, r=row, c=col: self.set_active_entry(r, c))
                entry.bind("<Return>", lambda e, r=row, c=col, ent=entry: self.update_cell(r, c, ent.get()))
                entry.bind("<FocusOut>", lambda e, r=row, c=col, ent=entry: self.update_cell(r, c, ent.get()))

                # Arrow key navigation
                entry.bind("<Up>", lambda e, r=row, c=col: self.navigate(r - 1, c))
                entry.bind("<Down>", lambda e, r=row, c=col: self.navigate(r + 1, c))
                entry.bind("<Left>", lambda e, r=row, c=col: self.navigate(r, c - 1))
                entry.bind("<Right>", lambda e, r=row, c=col: self.navigate(r, c + 1))
                entry.bind("<Shift-Return>", lambda e, r=row, c=col: self.navigate(r - 1, c))  # Move up on Shift+Enter
                entry.bind("<Return>", lambda e, r=row, c=col: self.navigate(r + 1, c))  # Move down on Enter

    def set_active_entry(self, row, col):
        self.active_entry = (row, col)

    def stop_editing(self, event):
        """Stop editing the active cell when clicking outside."""
        if self.active_entry:
            row, col = self.active_entry
            entry_widget = self.frame.grid_slaves(row=row + 1, column=col + 1)[0]
            self.update_cell(row, col, entry_widget.get())

            # Remove focus from the entry widget explicitly
            self.root.focus()  # Shift focus to the root window
            self.active_entry = None

    def navigate(self, row, col):
        """Move focus to the specified cell if within bounds."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            entry_widget = self.frame.grid_slaves(row=row + 1, column=col + 1)
            if entry_widget:
                entry_widget[0].focus_set()

    def update_cell(self, row, col, value):
        self.cells[row][col].set_value(value)
        print(f"Updated Cell({row}, {col}) to '{value}'")
