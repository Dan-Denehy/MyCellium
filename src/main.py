import tkinter as tk
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

#TODO: File Operations:
# - [ ] Save spreadsheet to a CSV file.
# - [ ] Load spreadsheet from a CSV file.

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

    # Create the GridView inside the main window
    grid_view = GridView(root, rows=10, cols=10)
    grid_view.frame.pack(expand=True, fill="both")  # Pack the frame to display it

    root.mainloop()

if __name__ == "__main__":
    main()
