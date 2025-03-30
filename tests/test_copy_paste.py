import sys
import os
import time
import unittest
import tkinter as tk
from unittest.mock import patch
from ui.grid_view import GridView
from ui.menu import paste_content, copy_content, cut_content

# Fixing the Python path issue
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestMenuAndShortcuts(unittest.TestCase):

    def setUp(self):
        """Set up a mock environment for testing."""
        self.root = tk.Tk()
        self.grid_view = GridView(self.root, rows=5, cols=5)

    def tearDown(self):
        """Destroy the mock environment."""
        self.root.destroy()

    def test_paste_from_menu(self):
        """Test the paste operation from the menu."""
        self.root.clipboard_clear()
        self.root.clipboard_append("Hello, Menu!")
        self.root.update()

        row, col = 1, 1
        self.grid_view.set_active_entry(row, col)
        paste_content(self.grid_view)

        pasted_value = self.grid_view.get_cell_value(row, col)
        self.assertEqual(pasted_value, "Hello, Menu!")
        print(f"Menu Paste Test: Expected 'Hello, Menu!', got '{pasted_value}'")

    def test_copy_from_menu(self):
        """Test the copy operation from the menu."""
        row, col = 2, 2
        test_value = "Copy Menu"
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, test_value)

        # Call the copy function via the menu
        copy_content(self.grid_view)

        # Get clipboard content
        clipboard_value = self.root.clipboard_get()
        self.assertEqual(clipboard_value, test_value)
        print(f"Menu Copy Test: Expected '{test_value}', got '{clipboard_value}'")

    def test_cut_from_menu(self):
        """Test the cut operation from the menu."""
        row, col = 3, 3
        test_value = "Cut Menu"
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, test_value)

        # Call the cut function via the menu
        cut_content(self.grid_view)

        # Get clipboard content
        clipboard_value = self.root.clipboard_get()
        cell_value = self.grid_view.get_cell_value(row, col)

        self.assertEqual(clipboard_value, test_value)
        self.assertEqual(cell_value, "")
        print(f"Menu Cut Test: Expected clipboard '{test_value}' and cell '', got clipboard '{clipboard_value}' and cell '{cell_value}'")

    def test_copy_shortcut(self):
        """Test the copy operation via Ctrl+C."""
        row, col = 1, 1
        test_value = "Shortcut Copy"
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, test_value)

        # Trigger the shortcut
        copy_content(self.grid_view)

        # Check the clipboard content
        clipboard_value = self.root.clipboard_get()
        print(f"Clipboard after copy: '{clipboard_value}'")
        self.assertEqual(clipboard_value, test_value)
        print(f"Keyboard Copy Test: Expected clipboard '{test_value}', got '{clipboard_value}'")

    def test_cut_shortcut(self):
        """Test the cut operation via shortcut (simulating function call)."""
        row, col = 2, 2
        test_value = "Shortcut Cut"
        self.grid_view.set_active_entry(row, col)
        self.grid_view.update_cell(row, col, test_value)

        # Directly call the cut function as a simulation of the keybind
        cut_content(self.grid_view)

        # Check clipboard and cell content
        clipboard_value = self.root.clipboard_get()
        cell_value = self.grid_view.get_cell_value(row, col)

        print(f"Clipboard after cut: '{clipboard_value}'")
        print(f"Cell value after cut: '{cell_value}'")

        self.assertEqual(clipboard_value, test_value)
        self.assertEqual(cell_value, "")
        print(
            f"Keyboard Cut Test: Expected clipboard '{test_value}' and cell '', got clipboard '{clipboard_value}' and cell '{cell_value}'")

    @patch('tkinter.Tk.clipboard_get', return_value="Shortcut Paste")
    def test_paste_shortcut(self, mock_clipboard_get):
        """Test the paste operation via shortcut (simulating function call)."""
        row, col = 3, 3
        self.grid_view.set_active_entry(row, col)

        # Directly call the paste function as a simulation of the keybind
        paste_content(self.grid_view)

        # Check the pasted value
        pasted_value = self.grid_view.get_cell_value(row, col)
        print(f"Cell value after paste: '{pasted_value}'")
        self.assertEqual(pasted_value, "Shortcut Paste")
        print(f"Keyboard Paste Test: Expected 'Shortcut Paste', got '{pasted_value}'")


if __name__ == "__main__":
    unittest.main()
