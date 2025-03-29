def rgba_to_hex(r, g, b, a=255):
    """
    Convert RGBA values to a hexadecimal color code.

    Args:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)
        a (int): Alpha component (0-255), default is 255 (opaque)

    Returns:
        str: Hexadecimal color code (e.g., #RRGGBB)
    """
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("RGB values must be in the range 0-255")
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
