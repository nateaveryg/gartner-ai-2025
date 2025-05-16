# name_formatter.py

def format_name(first_name, last_name, middle_initial=None):
    """
    Formats a person's name into a standard string format.
    The typical output is 'First M. Last' if a middle initial is provided,
    or 'First Last' otherwise.

    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        middle_initial (str, optional): The person's middle initial.
            Defaults to None. If provided, it's processed to be a
            single uppercase letter followed by a period (e.g., 'P.').
            Handles leading/trailing spaces and multi-character inputs
            by taking the first character.

    Returns:
        str: The formatted name string.
    """
    name_parts = [first_name.strip()] if first_name and first_name.strip() else [] # Initialize with stripped first_name if valid

    # Process middle initial if provided
    if middle_initial is not None:  # Ensure a middle initial was actually given
        cleaned_middle_initial = middle_initial.strip()
        if cleaned_middle_initial:  # Proceed if the initial is not just whitespace
            # Normalize to a single capitalized character with a period
            processed_initial = cleaned_middle_initial[0].upper() + "."
            name_parts.append(processed_initial)

    # Add stripped last_name if valid
    if last_name and last_name.strip():
        name_parts.append(last_name.strip())

    return " ".join(name_parts)


if __name__ == "__main__":
    print("Welcome to the AI-enhanced Name Formatter!")
    print(f"John Doe: {format_name('John', 'Doe')}")
    print(f"Jane Alice Smith: {format_name('Jane', 'Smith', 'Alice')}")
    print(f"Peter Paul Jones: {format_name('Peter', 'Jones', 'p')}") # Example with a lowercase middle initial
    print(f"Sarah Q. Davis: {format_name('Sarah', 'Davis', 'Q')}")
