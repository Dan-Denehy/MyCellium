import re

def check_function(value):
    """
        check if the value is a function (first char is '=')

        Args:
            value (str): The value to be checked.

        Returns:
            bool: True if the value meets the conditions (starts with '='); False otherwise.
    """
    if value is None:
        return False
    if value == '':
        return False
    if len(value) >= 0:
        return value[0] == '='
    return False


def cell_to_row_col(cell):
    """
    Converts a cell reference (e.g., 'A1', 'F2') to a zero-indexed (row, col) tuple.

    Args:
        cell (str): The cell reference in the format 'ColumnRow' (e.g., 'A1', 'F2', 'AA100').

    Returns:
        tuple: A tuple (row, col), where row and col are zero-indexed.
    """
    # Split the cell reference into letters (column) and digits (row)
    column = ''.join(filter(str.isalpha, cell))  # Get the letters (e.g., 'A', 'F', 'AA')
    row = ''.join(filter(str.isdigit, cell))  # Get the digits (e.g., '1', '100')

    # Convert the column from letters to a zero-indexed column number
    col_index = 0
    for char in column:
        col_index = col_index * 26 + (ord(char.upper()) - ord('A') + 1)  # Convert each letter to a base-26 number
    col_index -= 1  # Convert to zero-based index

    # Convert the row number to zero-based index
    row_index = int(row) - 1

    return row_index, col_index


# Example usage:
cell = "A1"
row, col = cell_to_row_col(cell)
print(f"Cell {cell} is at row {row}, column {col}")  # Output: Cell A1 is at row 0, column 0

cell = "F1"
row, col = cell_to_row_col(cell)
print(f"Cell {cell} is at row {row}, column {col}")  # Output: Cell F1 is at row 0, column 5

cell = "AA100"
row, col = cell_to_row_col(cell)
print(f"Cell {cell} is at row {row}, column {col}")  # Output: Cell AA100 is at row 99, column 26


def evaluate_expression(expression, gridView):
    """
    Evaluates an arithmetic expression with cell references (e.g., 'A1', 'B2', 'AA100') in the format 'A1+B2'.
    Replaces variables with corresponding values from the 'spreadsheet_data'.

    Args:
        expression (str): The arithmetic expression to evaluate.

    Returns:
        result (float): The evaluated result of the expression.
    """
    # Find all cell references (e.g., 'A1', 'B2', 'AA100')
    variables = re.findall(r'[A-Za-z]+\d+', expression)  # Matches patterns like A1, AA100, etc.


    for var in variables:
        row, col = cell_to_row_col(var)
        value = gridView.get_cell_display_value(row, col)
        expression = expression.replace(var, str(value))


    # Now evaluate the expression (using eval here for simplicity)
    try:
        result = eval(expression)  # Evaluate the final expression with replaced values
        return result
    except Exception as e:
        return f"Error: {e}"




def arithmetic_function(value, gridView):
    value = value[1:]
    value = value.replace(" ", "")
    # should now be in format (Letter(s)Number(s))
    evaluated = evaluate_expression(value, gridView)
    return evaluated