import tkinter as tk
from core.cell import Cell
from config.settings import HEADER_BG_COLOR, HEADER_TEXT_COLOR, CELL_FONT, HEADER_FONT, CELL_WIDTH
from ui.menu import copy_content, cut_content, paste_content




# Flashing border colors
FLASH_COLOR_1 = "#AE99C0"  # Light purple
FLASH_COLOR_2 = "black"    # Black

class GridView:
    def __init__(self, root, rows=10, cols=10):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.active_entry = None  # Track the currently active cell
        self.selected_entry = None

        # Create a frame to hold the grid
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")
        self.root.bind("<Escape>", lambda event: root.focus())
        # Key bindings for copy, cut, and paste
        self.root.bind("<Control-c>", lambda e: copy_content(self))
        self.root.bind("<Control-x>", lambda e: cut_content(self))
        self.root.bind("<Control-y>", lambda e: paste_content(self))

        self.create_grid()

    def create_grid(self):
        # Create column headers (A, B, C, ...)
        for col in range(self.cols):
            header = tk.Entry(
                self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                font=HEADER_FONT, readonlybackground=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR,
                    borderwidth=5, highlightthickness=2, highlightbackground="black"
            )
            header.insert(0, chr(65 + col))
            header.config(state="readonly")
            header.grid(row=0, column=col + 1, padx=0, pady=0, sticky="nsew")

        # Create row headers (1, 2, 3, ...)
        for row in range(self.rows):
            header = tk.Entry(
                self.frame, width=CELL_WIDTH, justify="center", relief="ridge",
                font=HEADER_FONT, readonlybackground=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR,
                    borderwidth=5, highlightthickness=2, highlightbackground="black"
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
                    borderwidth=1, highlightthickness=1, highlightbackground="black"
                )
                entry.grid(row=row + 1, column=col + 1, padx=0, pady=0, sticky="nsew")
                entry.insert(0, cell.get_value())
                entry.bind("<FocusIn>", lambda e, r=row, c=col: self.set_active_entry(r, c))
                entry.bind("<Return>", lambda e, r=row, c=col, ent=entry: self.update_cell(r, c, ent.get()))
                entry.bind("<FocusOut>", lambda e, r=row, c=col: self.stop_editing(e, r, c))
                # Double-click or press a key to start editing
                entry.bind("<Double-1>", lambda e, r=row, c=col: self.start_editing(r, c))
                entry.bind("<Key>", lambda e, r=row, c=col: self.start_editing(r, c))

                # Arrow key navigation
                entry.bind("<Up>", lambda e, r=row, c=col: self.navigate(r - 1, c))
                entry.bind("<Down>", lambda e, r=row, c=col: self.navigate(r + 1, c))
                entry.bind("<Left>", lambda e, r=row, c=col: self.navigate(r, c - 1))
                entry.bind("<Right>", lambda e, r=row, c=col: self.navigate(r, c + 1))
                entry.bind("<Shift-Return>", lambda e, r=row, c=col: self.navigate(r - 1, c))  # Move up on Shift+Enter
                entry.bind("<Return>", lambda e, r=row, c=col: self.navigate(r + 1, c))  # Move down on Enter



    def set_active_entry(self, row, col):
        """Sets the active cell without entering edit mode."""
        self.active_entry = (row, col)
        self.selected_entry = self.frame.grid_slaves(row=row + 1, column=col + 1)[0]

        # Make the Entry appear as a label by temporarily disabling it
        self.selected_entry.config(highlightbackground=FLASH_COLOR_2, highlightcolor=FLASH_COLOR_2, relief="ridge",
                                   borderwidth=1, state="readonly", readonlybackground="white")

        # Print the selected cell and value
        print(f"Selected Cell({row}, {col}) with value: '{self.cells[row][col].get_value()}'")
        self.flash_border()

    def flash_border(self):
        """Flashes the border of the selected cell."""
        if self.selected_entry:
            current_color = self.selected_entry.cget("highlightbackground")
            new_color = FLASH_COLOR_1 if current_color == FLASH_COLOR_2 else FLASH_COLOR_2
            self.selected_entry.config(
                highlightbackground=new_color, highlightcolor=new_color,
                relief="ridge", borderwidth=1  # Keep the border width consistent
            )
            # Schedule the next flash and store the callback ID
            self.flash_id = self.selected_entry.after(600, self.flash_border)

    def start_editing(self, row, col):
        """Start editing the cell only when double-clicked."""
        print(f"Double-clicked to edit cell({row}, {col})")
        if self.active_entry:
            r, c = self.active_entry
            entry_widget = self.frame.grid_slaves(row=r + 1, column=c + 1)[0]

            # Enable the Entry for editing and set focus
            entry_widget.config(state="normal")
            entry_widget.focus_set()
            print(f"Editing Cell({r}, {c})")

    def stop_editing(self, event, row=None, col=None):
        """Stop editing the active cell when clicking outside or switching cells."""
        print(f"row={row}, col={col}")

        if row is not None and col is not None:
            if self.active_entry is not None:
                print("closing edit and saving")
                entry_widget = self.frame.grid_slaves(row=self.active_entry[0] + 1, column=self.active_entry[1] + 1)[0]

                # Stop the flashing effect if it is active
                if hasattr(self, 'flash_id'):
                    self.selected_entry.after_cancel(self.flash_id)

                # Reset the border color and width to normal when losing focus
                entry_widget.config(highlightbackground=FLASH_COLOR_2, highlightcolor=FLASH_COLOR_2, relief="ridge", borderwidth=1, state="readonly", readonlybackground="white")

                # Update the cell value
                self.update_cell(self.active_entry[0], self.active_entry[1], entry_widget.get())

    def navigate(self, row, col):
        """Move focus to the specified cell if within bounds."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            entry_widget = self.frame.grid_slaves(row=row + 1, column=col + 1)
            if entry_widget:
                entry_widget[0].focus_set()

    def update_cell(self, row, col, value):
        self.cells[row][col].set_value(value)
        print(f"Updated Cell({row}, {col}) to '{value}'")

    def get_cell_value(self, row, col):
        """Return the value of the cell at the given row and column."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.cells[row][col].get_value()
        return None
