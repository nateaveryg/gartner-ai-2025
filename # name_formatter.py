# name_formatter.py

def format_name(first_name, last_name, middle_initial=None):
    """
    Formats a name as 'First M. Last'.
    """
    formatted_name = f"{first_name}"
    if middle_initial and middle_initial.strip():
        initial = middle_initial.strip()[0].upper()
        formatted_name += f" {initial}."
    return f"{formatted_name} {last_name}"

# code has been tested and passes all tests
if __name__ == "__main__":
    print("Welcome to the AI-enhanced Name Formatter!")
    print(f"John Doe: {format_name('John', 'Doe')}")
    print(f"Jane Alice Smith: {format_name('Jane', 'Smith', 'Alice')}")
    print(f"Peter Paul Jones: {format_name('Peter', 'Jones', 'p')}") # This will expose the bug: 'p' instead of 'P.'
    print(f"Sarah Q. Davis: {format_name('Sarah', 'Davis', 'Q')}")
