import tkinter as tk
from tkinter import filedialog, messagebox

# To store copied content for cut/copy/paste
clipboard = ""

def new_spreadsheet(grid_view):
    """Clear the entire spreadsheet."""
    for row in range(grid_view.rows):
        for col in range(grid_view.cols):
            grid_view.cells[row][col].set_value("")
            entry_widget = grid_view.frame.grid_slaves(row=row + 1, column=col + 1)
            if entry_widget:
                entry_widget[0].delete(0, tk.END)
    print("Spreadsheet cleared!")

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
                                entry_widget[0].delete(0, tk.END)
                                entry_widget[0].insert(0, value.strip())
            print(f"Loaded from {filepath}")
        except Exception as e:
            print(f"Error loading file: {e}")


def cut_content(grid_view):
    """Perform a cut operation: copy content to clipboard and clear cell."""
    # Reuse the copy function
    copy_content(grid_view)

    row, col = grid_view.active_entry
    entry_widget = grid_view.frame.grid_slaves(row=row + 1, column=col + 1)[0]

    try:
        # Clear the cell content after copying
        entry_widget.delete(0, tk.END)
        grid_view.update_cell(row, col, "")
        print(f"Cut content: '' from ({row}, {col})")
    except Exception as e:
        print(f"Cut error: {e}")


def copy_content(grid_view):
    row, col = grid_view.active_entry


    # Get the cell's current value
    content = grid_view.get_cell_value(row, col)

    try:
        # Clear the clipboard and add the content
        grid_view.root.clipboard_clear()
        grid_view.root.clipboard_append(content)

        # Force the clipboard update and maintain focus
        grid_view.root.update_idletasks()
        grid_view.root.update()
        print(f"Copied content: {content} from ({row}, {col})")
    except Exception as e:
        print(f"Copy error: {e}")


def paste_content(grid_view):
    row, col = grid_view.active_entry
    try:
        # Get the content from the system clipboard
        clipboard = grid_view.root.clipboard_get()

        # Get the corresponding entry widget
        entry_widget = grid_view.frame.grid_slaves(row=row + 1, column=col + 1)[0]

        # Set the entry to normal state for editing
        entry_widget.config(state="normal")
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, clipboard)

        # Properly update the cell through the update method
        grid_view.update_cell(row, col, clipboard)
        print(f"Pasted content: {clipboard} at ({row}, {col})")
    except Exception as e:
        print(f"Paste error: {e}")








def about():
    messagebox.showinfo("About", "MyCellium Spreadsheet App v0")

def create_menu(root, grid_view):
    """Creates an Excel-like menu bar with color and underlines."""
    # Set global menu font using option_add
    root.option_add('*Menu.font', 'Times 12 bold')

    menu_bar = tk.Menu(root)

    # File Menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", underline=0, command=lambda: new_spreadsheet(grid_view))
    file_menu.add_command(label="Open", underline=0, command=lambda: load_from_csv(grid_view))
    file_menu.add_command(label="Save", underline=0, command=lambda: save_to_csv(grid_view))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", underline=1, command=root.quit)
    menu_bar.add_cascade(label="File", underline=0, menu=file_menu)

    # Edit Menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Undo", underline=0, command=lambda: print("Undo (placeholder)"))
    edit_menu.add_command(label="Redo", underline=0, command=lambda: print("Redo (placeholder)"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", underline=2, command=lambda: cut_content(grid_view))
    edit_menu.add_command(label="Copy", underline=0, command=lambda: copy_content(grid_view))
    edit_menu.add_command(label="Paste", underline=0, command=lambda: paste_content(grid_view))
    menu_bar.add_cascade(label="Edit", underline=0, menu=edit_menu)

    # Help Menu
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", underline=0, command=about)
    menu_bar.add_cascade(label="Help", underline=0, menu=help_menu)

    root.config(menu=menu_bar)
