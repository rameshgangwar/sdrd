import pandas as pd
import json
import os

# --- Configuration ---
# The name of your Excel file.
EXCEL_FILE_NAME = 'studentData.xlsx'
# The name of the output JavaScript file.
JS_OUTPUT_FILE_NAME = 'studentData.js'
# The name of the JavaScript variable to hold the data.
JS_VARIABLE_NAME = 'STUDENT_DATA'
# --- End of Configuration ---

def convert_excel_to_js():
    """
    Reads data from an Excel file and converts it into a JavaScript file
    that assigns the data to a constant.
    """
    # Get the directory where the script is located
    script_dir = os.path.dirname(__file__)
    excel_file_path = os.path.join(script_dir, EXCEL_FILE_NAME)
    js_output_path = os.path.join(script_dir, JS_OUTPUT_FILE_NAME)

    # Check if the Excel file exists
    if not os.path.exists(excel_file_path):
        print(f"❌ Error: Excel file not found at '{excel_file_path}'")
        print("Please make sure the Excel file is in the same directory as this script.")
        return

    try:
        # Read the Excel file. `openpyxl` must be installed.
        # The `dtype=str` argument ensures all data, like SR numbers, is read as text.
        df = pd.read_excel(excel_file_path, dtype=str)

        # Convert the DataFrame to a list of dictionaries
        records = df.to_dict(orient='records')

        # Convert the list of dictionaries to a JSON string with indentation
        json_data = json.dumps(records, indent=4)

        # Create the JavaScript file content
        js_content = f"const {JS_VARIABLE_NAME} = {json_data};\n"

        # Write the content to the JavaScript file
        with open(js_output_path, 'w', encoding='utf-8') as f:
            f.write(js_content)

        print(f"✅ Success! Converted {len(records)} records from '{EXCEL_FILE_NAME}' to '{JS_OUTPUT_FILE_NAME}'.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == '__main__':
    convert_excel_to_js()