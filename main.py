import os
import google.generativeai as genai

# Configuring LLM with the API key
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.0-pro")

def extract_data_with_llm(url, schema):
    """
    Extracts data from a webpage using LLM and validates against schema

    Args:
        url: URL of the webpage
        schema: Dictionary defining desired data structure

    Returns:
        Dictionary containing extracted data or error message
    """
    prompt = f"""Extract data from the webpage {url} according to the schema: {schema}. 
    And if in schema there is format then make sure to format the 'format' field as a list of dictionaries, 
    where each dictionary represents a format type with its details. 
    Return in json format"""
    try:
        response = model.generate_content(prompt)
        data = response.text
        return data
    except Exception as e:
        return {"error": str(e)}