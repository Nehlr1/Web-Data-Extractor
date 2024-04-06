import streamlit as st
from main import extract_data_with_llm

def main():
    """
    Streamlit application for data extraction
    """
    st.title("Web Data Extractor")
    url = st.text_input("Product Link:")
    schema_keys = st.text_input("Schema (comma-separated keys):")

    if st.button("Get Data"):
        schema = {}
        if schema_keys:
            schema_keys = list(filter(None, schema_keys.split(",")))
            for key in schema_keys:
                schema[key.strip()] = "string"
        extracted_data = extract_data_with_llm(url, schema)
        st.write(extracted_data)

if __name__ == "__main__":
    main()