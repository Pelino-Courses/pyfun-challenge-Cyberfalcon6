def format_text(text: str, prefix: str = "", suffix: str = "", capitalize: bool = False, max_length: int = None) -> str:
    """
    Formats the given text based on the provided parameters.

    Args:
        text (str): The input text to format.
        prefix (str, optional): A string to prepend to the text. Defaults to "".
        suffix (str, optional): A string to append to the text. Defaults to "".
        capitalize (bool, optional): Whether to capitalize the text. Defaults to False.
        max_length (int, optional): The maximum length of the formatted text. Defaults to None.

    Returns:
        str: The formatted text.

    Raises:
        TypeError: If any argument is of an invalid type.
        ValueError: If max_length is not a positive integer.

    Examples:
        >>> format_text("hello", prefix=">>", suffix="<<", capitalize=True, max_length=10)
        '>>HELLO<<'

        >>> format_text("world", capitalize=True)
        'WORLD'
    """
    if not isinstance(text, str):
        raise TypeError("The 'text' argument must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("The 'prefix' argument must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("The 'suffix' argument must be a string.")
    if not isinstance(capitalize, bool):
        raise TypeError("The 'capitalize' argument must be a boolean.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' argument must be an integer.")
        if max_length <= 0:
            raise ValueError("The 'max_length' argument must be a positive integer.")

    formatted_text = f"{prefix}{text}{suffix}"
    if capitalize:
        formatted_text = formatted_text.upper()
    if max_length is not None and len(formatted_text) > max_length:
        formatted_text = formatted_text[:max_length]

    return formatted_text


if __name__ == "__main__":
    try:
        text = input("Enter the text to format: ")
        prefix = input("Enter a prefix (optional): ")
        suffix = input("Enter a suffix (optional): ")
        capitalize = input("Capitalize the text? (yes/no): ").strip().lower() == "yes"
        max_length = input("Enter the maximum length (optional): ")
        max_length = int(max_length) if max_length else None

        formatted = format_text(text, prefix, suffix, capitalize, max_length)
        print(f"Formatted text: {formatted}")
    except Exception as e:
        print(f"Error: {e}")