import tkinter as tk
from ui.menu import create_menu
from ui.grid_view import GridView

#TODO (v0 Requirements):
# - [x] Display a grid of cells (10x10 by default).
# - [x] Show row and column headers.
# - [x] Apply consistent header and cell styles (MyCellium theme).
# - [x] Click outside a cell to stop editing.

#TODO: Interaction:
# - [x] Edit cells by clicking and typing.
# - [x] Save changes on Enter or clicking outside.
# - [x] Navigate with arrow keys, Enter, and Shift+Enter.
# - [x] Ability to escape cell editing (uses 'Esc' Key)

#TODO: File Operations:
# - [X] Save spreadsheet to a CSV file.
# - [X] Load spreadsheet from a CSV file.

#TODO: Menu Bar:
# - [ ] Create a basic menu with Save, Load, and Exit options.

#TODO: Testing:
# - [x] Unit tests for UI support functions (like color conversion).
# - [ ] Manual testing for navigation and editing.

#TODO: CI/CD Integration:
# - [ ] Set up automated testing pipeline with GitHub Actions.
# - [ ] Implement basic linting for code consistency.


def main():
    root = tk.Tk()
    root.title("MyCellium Spreadsheet App")
    root.geometry("800x600")

    grid_view = GridView(root, rows=10, cols=10)

    # Create menu using the menu module
    create_menu(root, grid_view)

    root.mainloop()


if __name__ == "__main__":
    main()