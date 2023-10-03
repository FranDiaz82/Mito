import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import os

st.set_page_config(layout='wide')
st.title("Saving a Mito generated Python script to a .py file")

st.markdown("""This app demonstrates how to save a Mito generated Python script to a .py file.
1. Use the input field below to name your script. 
2. Click on the `Import Files` button in the Mito spreadsheet and import loans.csv.
3. Make a few edits to the data.
4. Click the `Save Generated Code to .py file` button below the spreadsheet.
5. Find the generated code located at `/scripts/{script_name}.py`.
""")

st.markdown("""Notice that the generated code is a function. This is the result of setting the `code_options` parameter to the spreadsheet component.""")

script_name = st.text_input('Script Name:', value='Automation Script')
script_name_cleaned = script_name.replace(' ', '_').lower()

_, generated_code = spreadsheet(
    import_folder = './data',
    code_options={
        'as_function': True, 
        'import_custom_python_code': True, 
        'call_function': True, 
        'function_name': f'function_{script_name_cleaned}', 
        'function_params': {}
    }
)

if st.button("Save Generated Code to .py file"):
    # When the user clicks the button, save the generated_code returned by the spreadsheet 
    # component to a .py file in the /scripts directory.
    file_path = os.path.join(os.getcwd(), 'scripts', script_name + '.py')
    with open(file_path, 'w') as f:
        f.write(generated_code)
        st.success(f"Saved generated the following code to {script_name}")
        st.code(generated_code)