import sys
import os
import unittest
import tkinter as tk
from ui.grid_view import GridView
from ui.menu import load_from_csv

"""
Test 1:
    1. Given: A cell containing an arithmetic expression (e.g., =A1+A2).
    2. When: The user inputs the expression and presses Enter.
    3. Then: The cell displays the calculated result.

Test 2:
    1. Given: A cell containing a division expression (e.g., =A1/A2) where A2 is zero.
    2. When: The user inputs the expression and presses Enter.
    3. Then: The cell displays an error message indicating division by zero.

Test 3:
    1. Given: A cell containing an invalid arithmetic expression (e.g., =A1+*A2).
    2. When: The user inputs the expression and presses Enter.
    3. Then: The cell displays an error message "#NAME?" indicating a syntax error.

Test 4:
    1. Given: A file containing expressions, the file should load with them evaluated if they are valid.
    2. When: The user loads a file with valid expressions.
    3. Then: The cells display the calculated answer instead of the expression.

Test 5:
    1. Given: A cell containing an expression, the cell should store the expression, but display the result.
    2. When: The user has an expression in a cell.
    3. Then: The cell displays the result of the function.

Test 6:
    1. Given: A cell containing an expression, the cell should display the expression when editing.
    2. When: The user edits a cell that is an expression.
    3. Then: The cells display the expression and allows the user to edit the expression.
"""


class ArithmeticAdvancedTest(unittest.TestCase):

    def setUp(self):
        """Set up a mock environment for testing."""
        self.root = tk.Tk()
        self.grid_view = GridView(self.root, rows=10, cols=10)

    def tearDown(self):
        """Destroy the mock environment."""
        self.root.destroy()

    # Test 1: Arithmetic expression evaluation (A1 + B1)
    def test_arithmetic_expression(self):
        # Set A1 (0,0)
        self.grid_view.set_active_entry(0, 0)
        self.grid_view.update_cell(0, 0, "3")

        # Set B1 (0,1)
        self.grid_view.set_active_entry(0, 1)
        self.grid_view.update_cell(0, 1, "4")

        # Set C1 (0,2) as =A1+B1
        self.grid_view.set_active_entry(0, 2)
        self.grid_view.update_cell(0, 2, "=A1+B1")

        result = self.grid_view.get_cell_display_value(0, 2)  # C1
        self.assertEqual(result, 7)

    # Test 2: Division by zero (A1 / B1)
    def test_division_by_zero(self):
        # Set A1 (0,0)
        self.grid_view.set_active_entry(0, 0)
        self.grid_view.update_cell(0, 0, "5")

        # Set B1 (0,1) to 0
        self.grid_view.set_active_entry(0, 1)
        self.grid_view.update_cell(0, 1, "0")

        # Set C1 (0,2) as =A1/B1
        self.grid_view.set_active_entry(0, 2)
        self.grid_view.update_cell(0, 2, "=A1/B1")

        result = self.grid_view.get_cell_display_value(0, 2)  # C1
        self.assertEqual(result, "#DIV/0!")

    # Test 3: Invalid arithmetic expression (A1 + * B1)
    def test_invalid_expression(self):
        # Set A1 (0,0) with invalid expression
        self.grid_view.set_active_entry(0, 0)
        self.grid_view.update_cell(0, 0, "=A1+*B1")

        result = self.grid_view.get_cell_display_value(0, 0)  # A1
        self.assertEqual(result, "#NAME?")

    # Test 4: Loading valid expressions from a file
    def test_load_valid_file(self):

        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "CSV_Files", "arithmetic_test.csv")
        load_from_csv(self.grid_view, file_path)


        result = self.grid_view.get_cell_display_value(0, 2)  # C1
        self.assertEqual(result, 4)

    # Test 5: Storing the expression while displaying the result
    def test_store_expression_display_result(self):
        # Set A1 (0,0) and B1 (0,1)
        self.grid_view.set_active_entry(0, 0)
        self.grid_view.update_cell(0, 0, "2")
        self.grid_view.set_active_entry(0, 1)
        self.grid_view.update_cell(0, 1, "3")

        # Set C1 (0,2) as =A1*B1
        self.grid_view.set_active_entry(0, 2)
        self.grid_view.update_cell(0, 2, "=A1*B1")

        stored = self.grid_view.cells[0][2].get_value()
        displayed = self.grid_view.get_cell_display_value(0, 2)
        self.assertEqual(stored, "=A1*B1")
        self.assertEqual(displayed, 6)

    # Test 6: Editing an expression to display the formula
    def test_edit_expression(self):
        # Set A1 (0,0) as =A1+B1
        self.grid_view.set_active_entry(0, 0)
        self.grid_view.update_cell(0, 0, "=A1+B1")
        self.grid_view.start_editing(0,0)


        entry = self.grid_view.frame.grid_slaves(row=self.grid_view.active_entry[0] + 1, column=self.grid_view.active_entry[1] + 1)[0]
        result = entry.get()
        self.assertEqual(result, "=A1+B1")


if __name__ == '__main__':
    unittest.main()