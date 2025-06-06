# Name Formatter Utility

This project provides a simple Python utility to format names. It can handle names with or without middle initials, ensuring consistent formatting.

## `format_name` Function

This is the core function of the utility.

**Purpose:** Takes a person's first name, last name, and an optional middle initial, and returns a formatted name string.

**Parameters:**

*   `first_name` (str): The person's first name.
*   `last_name` (str): The person's last name.
*   `middle_initial` (str, optional): The person's middle initial. Defaults to `None`.
    *   If provided, the initial is processed: whitespace is stripped, the first character is taken, capitalized, and a period is appended (e.g., "  j.  " becomes "J.").
    *   If `None`, an empty string, or a string with only whitespace, it's ignored.

**Returns:**

*   (str): A string containing the formatted name (e.g., "First M. Last" or "First Last").

**Examples:**

```python
from name_formatter import format_name

# Example without a middle initial
name1 = format_name("John", "Doe")
print(name1)  # Output: John Doe

# Example with a middle initial
name2 = format_name("Jane", "Smith", "M")
print(name2)  # Output: Jane M. Smith

# Example with a lowercase middle initial and extra spaces
name3 = format_name("Peter", "Jones", "  p  ")
print(name3)  # Output: Peter P. Jones

# Example with a middle initial already having a period
name4 = format_name("Sarah", "Davis", "Q.")
print(name4)  # Output: Sarah Q. Davis
```

*Note: The actual filename for importing is `# name_formatter.py` due to a '#' in its name. So the import statement should be `from \`# name_formatter\` import format_name` if you are running it directly. However, when used as a module, Python's import system might handle it differently or it might be advisable to rename the file for broader compatibility.*
## How to Use

1.  **Import the function:**

    ```python
    from \`# name_formatter\` import format_name
    ```
    *(Please note the filename `# name_formatter.py`. If you encounter issues with the import due to the '#' character, consider renaming the file to `name_formatter.py` and adjusting the import statement accordingly: `from name_formatter import format_name`)*

2.  **Call the function:**

    ```python
    full_name = format_name("YourFirstName", "YourLastName", "Y")
    print(full_name)

    full_name_no_middle = format_name("AnotherFirstName", "AnotherLastName")
    print(full_name_no_middle)
    ```
## Running Tests

This project includes a suite of unit tests to ensure the `format_name` function behaves as expected. The tests are located in the `test_name_formatter.py` file.

To run the tests, navigate to the project's root directory in your terminal and execute the following command:

```bash
python -m unittest test_name_formatter.py
```
