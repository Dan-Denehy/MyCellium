import sys
import os
import time
import unittest
import tkinter as tk
from unittest.mock import patch
from ui.grid_view import GridView
from ui.menu import load_from_csv


class LoadWithFunctionsTest(unittest.TestCase):

    def setUp(self):
        """Set up a mock environment for testing."""
        self.root = tk.Tk()
        self.grid_view = GridView(self.root, rows=4, cols=10)

    def tearDown(self):
        """Destroy the mock environment."""
        self.root.destroy()

    def test_simple_addition(self):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "CSV_Files", "arithmetic_test.csv")
        load_from_csv(self.grid_view, file_path)
        cell_value = self.grid_view.get_cell_display_value(2, 2)

        self.assertEqual(cell_value, 30)

if __name__ == '__main__':
    unittest.main()
