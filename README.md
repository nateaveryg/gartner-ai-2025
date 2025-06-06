# Name Formatter Utility

This project provides a simple Python utility and a web interface to format names. It can handle names with or without middle initials, ensuring consistent formatting.

## Project Structure

The project is organized as follows:

*   **Root Directory**: Contains the Python backend API (`api.py`), the core name formatting logic (`# name_formatter.py`), and their respective tests (`test_api.py`, `test_name_formatter.py`).
*   **`frontend/` Directory**: Contains the Next.js/React frontend application.

## `format_name` Function (Core Logic)

This is the core function of the utility, found in `# name_formatter.py`.

**Purpose:** Takes a person's first name, last name, and an optional middle initial, and returns a formatted name string.

**Parameters:**

*   `first_name` (str): The person's first name.
*   `last_name` (str): The person's last name.
*   `middle_initial` (str, optional): The person's middle initial. Defaults to `None`.
    *   If provided, the initial is processed: whitespace is stripped, the first character is taken, capitalized, and a period is appended (e.g., "  j.  " becomes "J.").
    *   If `None`, an empty string, or a string with only whitespace, it's ignored.

**Returns:**

*   (str): A string containing the formatted name (e.g., "First M. Last" or "First Last").

## Running the Application

### Backend API (Python/Flask)

The backend is a Flask application serving the name formatting logic.

1.  **Navigate to the project root directory.**
2.  **Install dependencies:**
    ```bash
    pip install Flask
    ```
3.  **Run the API server:**
    ```bash
    python api.py
    ```
    The API will be available at `http://localhost:5000`. The primary endpoint is `/api/format_name`.

### Frontend (Next.js/React)

The frontend is a Next.js/React application providing a user interface to interact with the API.

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd frontend
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
    *(If you encounter issues, ensure you have Node.js and npm installed.)*
3.  **Run the development server:**
    ```bash
    npm run dev
    ```
    The frontend application will be available at `http://localhost:3000`.

## Running Tests

### Core Logic Tests

Unit tests for the `format_name` function are in `test_name_formatter.py`.

1.  **Navigate to the project root directory.**
2.  **Run the tests:**
    ```bash
    python -m unittest test_name_formatter.py
    ```

### API Tests

Integration tests for the API endpoints are in `test_api.py`. These tests require the Flask API server to be running.

1.  **Ensure the Backend API is running** (see "Backend API (Python/Flask)" section above).
2.  **Navigate to the project root directory.**
3.  **Run the API tests:**
    ```bash
    python -m unittest test_api.py
    ```

*Note on `# name_formatter.py`: The core logic file `# name_formatter.py` has a leading '#' in its name. `api.py` uses `importlib` to load it. The tests in `test_name_formatter.py` also use `importlib` or assume direct execution context where this might be less problematic.*
