class Cell:
    def __init__(self, row, col, value=""):
        self.row = row
        self.col = col
        self.value = value

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def __repr__(self):
        return f"Cell({self.row}, {self.col}, '{self.value}')"