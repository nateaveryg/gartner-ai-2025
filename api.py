from flask import Flask, request, jsonify
import importlib.util

# Load # name_formatter.py module
# The name "name_formatter_module" is an arbitrary name for the loaded module object.
spec = importlib.util.spec_from_file_location("name_formatter_module", "# name_formatter.py")
name_formatter_module = importlib.util.module_from_spec(spec)
# Ensure the loader executes the module to make its contents available.
# This step can raise an ImportError if the file doesn't exist or has syntax errors.
spec.loader.exec_module(name_formatter_module)
format_name = name_formatter_module.format_name

app = Flask(__name__)

@app.route('/api/format_name', methods=['GET'])
def handle_format_name():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    middle_initial = request.args.get('middle_initial')

    # Call the imported format_name function
    formatted_name_str = format_name(
        first_name=first_name,
        last_name=last_name,
        middle_initial=middle_initial
    )
    return jsonify(formatted_name=formatted_name_str)

if __name__ == '__main__':
    # Port specified to avoid potential conflicts and for clarity.
    app.run(debug=True, port=5000)
