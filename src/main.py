import tkinter as tk
from ui.grid_view import GridView

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
