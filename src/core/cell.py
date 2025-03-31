class Cell:
    def __init__(self, row, col, value=""):
        self.row = row
        self.col = col
        self.value = value
        self.display_value = value
        self.is_editing = False

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def set_display_value(self, new_value):
        self.display_value = new_value

    def get_display_value(self):
        return self.display_value

    def set_editing(self, is_editing):
        """Set the editing flag."""
        self.is_editing = is_editing

    def is_in_edit_mode(self):
        """Check if the cell is currently being edited."""
        return self.is_editing

    def __repr__(self):
        return f"Cell({self.row}, {self.col}, '{self.value}', '{self.display_value}')"

