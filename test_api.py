import unittest
import json
import urllib.request
import urllib.parse

class TestApi(unittest.TestCase):

    BASE_URL = "http://localhost:5000/api/format_name"

    def _make_request(self, params):
        """Helper function to make a request and return status and data."""
        query_string = urllib.parse.urlencode(params)
        url = f"{self.BASE_URL}?{query_string}"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                status = response.status
                data = json.loads(response.read().decode())
                return status, data
        except urllib.error.HTTPError as e:
            # For HTTP errors, try to read the response body if possible
            # as it might contain a JSON error message from Flask.
            error_data = None
            try:
                error_data = json.loads(e.read().decode())
            except Exception:
                pass # Ignore if error body is not JSON or not readable
            return e.code, error_data or {"error": f"HTTPError: {e.code} {e.reason}"}
        except Exception as e:
            # Catch other errors like connection refused, timeout
            return None, {"error": str(e)}

    def test_format_name_endpoint_success_with_middle(self):
        """Test /api/format_name with first, middle, and last name."""
        status, data = self._make_request({
            "first_name": "John",
            "middle_initial": "M",
            "last_name": "Doe"
        })
        self.assertEqual(status, 200, msg=f"API call failed with data: {data}")
        self.assertIn("formatted_name", data)
        self.assertEqual(data["formatted_name"], "John M. Doe")

    def test_format_name_endpoint_success_no_middle(self):
        """Test /api/format_name with first and last name only."""
        status, data = self._make_request({
            "first_name": "Jane",
            "last_name": "Doe"
        })
        self.assertEqual(status, 200, msg=f"API call failed with data: {data}")
        self.assertIn("formatted_name", data)
        self.assertEqual(data["formatted_name"], "Jane Doe")

    def test_format_name_endpoint_success_middle_with_dot(self):
        """Test /api/format_name with middle initial already having a dot."""
        status, data = self._make_request({
            "first_name": "Peter",
            "middle_initial": "P.",
            "last_name": "Jones"
        })
        self.assertEqual(status, 200, msg=f"API call failed with data: {data}")
        self.assertIn("formatted_name", data)
        self.assertEqual(data["formatted_name"], "Peter P. Jones")

    def test_format_name_endpoint_success_lowercase_middle(self):
        """Test /api/format_name with lowercase middle initial."""
        status, data = self._make_request({
            "first_name": "Sarah",
            "middle_initial": "q",
            "last_name": "Davis"
        })
        self.assertEqual(status, 200, msg=f"API call failed with data: {data}")
        self.assertIn("formatted_name", data)
        self.assertEqual(data["formatted_name"], "Sarah Q. Davis")

    def test_format_name_endpoint_empty_middle(self):
        """Test /api/format_name with an empty middle initial."""
        status, data = self._make_request({
            "first_name": "Alice",
            "middle_initial": "",
            "last_name": "Wonderland"
        })
        self.assertEqual(status, 200, msg=f"API call failed with data: {data}")
        self.assertIn("formatted_name", data)
        self.assertEqual(data["formatted_name"], "Alice Wonderland")

    def test_format_name_endpoint_missing_firstname(self):
        """Test /api/format_name with missing first_name parameter."""
        # Flask's default behavior for missing request.args.get() is None,
        # which our format_name function might treat as an error or empty.
        # The current format_name function would raise a TypeError if first_name is None.
        # The Flask app's error handling for this is a 500 Internal Server Error.
        status, data = self._make_request({
            "last_name": "Doe"
        })
        self.assertEqual(status, 500, msg=f"API did not return 500 for missing first_name. Data: {data}")
        # Depending on Flask's error formatting, the response might be HTML or JSON.
        # For a robust test, you might check if it's a JSON error with a specific message,
        # but that requires api.py to have a proper error handler for TypeErrors.
        # For now, just checking the status code is a basic verification.
        # self.assertIn("error", data) # This might fail if Flask returns HTML for 500

    def test_format_name_endpoint_missing_lastname(self):
        """Test /api/format_name with missing last_name parameter."""
        status, data = self._make_request({
            "first_name": "John"
        })
        self.assertEqual(status, 500, msg=f"API did not return 500 for missing last_name. Data: {data}")

if __name__ == '__main__':
    unittest.main()
