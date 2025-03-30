import sys
import os
import time
import unittest
import tkinter as tk
from unittest.mock import patch
from ui.grid_view import GridView


class ArithmeticTest(unittest.TestCase):

    def setUp(self):
        """Set up a mock environment for testing."""
        self.root = tk.Tk()
        self.grid_view = GridView(self.root, rows=5, cols=5)

    def tearDown(self):
        """Destroy the mock environment."""
        self.root.destroy()

    def test_simple_addition(self):
        row = col = 0
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, "4")
        row += 1
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, "3")
        row += 1
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, "2")
        row = 0
        col += 1
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, "=A1+A2")
        row += 1
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, "=B1*A3")
        row += 1
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, "=Hi")


        result = self.grid_view.get_cell_display_value(0,1)
        self.assertEqual(result, 7)
        result = self.grid_view.get_cell_display_value(1,1)
        self.assertEqual(result, 14)
        result = self.grid_view.get_cell_display_value(2,1)
        self.assertEqual(result, "#NAME?")

if __name__ == '__main__':
    unittest.main()
