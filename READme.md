 Web Data Extractor
===============

A simple web application built using Streamlit and Generative AI to extract data from a webpage according to a given schema.

Prerequisites
-------------

* Python 3.x
* [Streamlit](https://streamlit.io/)
* [Google GenerativeAI SDK](https://github.com/google/generative-ai-python)
* Environment variable `GEMINI_API_KEY` with your GenerativeAI API key

Getting Started
---------------

1. Clone the repository:

   ```
   git clone https://github.com/<username>/web-data-extractor.git
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set the environment variable with your API key:

   ```
   export GEMINI_API_KEY=<your_api_key>
   ```

4. Run the Streamlit application:

   ```
   streamlit run streamlit_app.py
   ```

Usage
-----

1. Enter the URL of the webpage you want to extract data from.
2. Enter the comma-separated keys of the schema. For example, `name, author, format`.
3. Click on the `Get Data` button to extract the data.

Example
-------

Suppose you want to extract data from the following URL:

```
https://www.example.com/product/123
```

And the schema for the data is as follows:

```
name, author, format
```

After running the Streamlit application, enter the above URL and schema and click on the `Get Data` button. The extracted data will be displayed as:

```
{
  "name": "Product Name",
  "author": "Author Name",
  "format": [
    {
      "type": "Paperback",
      "price": "16.99",
      "availability": "In stock"
    },
  ]
}
```