import tkinter as tk
from tkinter import filedialog


def save_to_csv(grid_view):
    filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if filepath:
        try:
            with open(filepath, 'w') as file:
                for row in grid_view.cells:
                    file.write(','.join([cell.get_value().strip() for cell in row]) + "\n")
            print(f"Saved to {filepath}")
        except Exception as e:
            print(f"Error saving file: {e}")



def load_from_csv(grid_view):
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                for row_idx, line in enumerate(file.readlines()):
                    values = line.strip().split(',')
                    for col_idx, value in enumerate(values):
                        if row_idx < len(grid_view.cells) and col_idx < len(grid_view.cells[row_idx]):
                            # Update the cell value
                            grid_view.cells[row_idx][col_idx].set_value(value.strip())

                            # Update the actual Entry widget on the grid
                            entry_widget = grid_view.frame.grid_slaves(row=row_idx + 1, column=col_idx + 1)
                            if entry_widget:
                                entry_widget[0].delete(0, tk.END)  # Clear existing text
                                entry_widget[0].insert(0, value.strip())  # Insert the new value
            print(f"Loaded from {filepath}")
        except Exception as e:
            print(f"Error loading file: {e}")



def create_menu(root, grid_view):
    menu_bar = tk.Menu(root)

    # File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Save", command=lambda: save_to_csv(grid_view))
    file_menu.add_command(label="Load", command=lambda: load_from_csv(grid_view))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    menu_bar.add_cascade(label="File", menu=file_menu)

    # Attach the menu to the root window
    root.config(menu=menu_bar)
