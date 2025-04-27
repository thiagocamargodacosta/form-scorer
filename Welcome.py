import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Form scorer - Welcome!", page_icon="👋")

# Using pages
st.markdown("# Welcome! 👋")

st.markdown(
    """
    This tool provides a way to automatically score forms from the following questionnaires:

    - DASS-21
    - PSQI-PT
    - PANAS

    After the scoring is done, you can download the result data and continue your data analysis process
    ### How to use
    1. 👈 Select the questionnaire on the sidebar
    2. Upload a `.csv` file containing the form data which you wish to obtain the scores
    3. A table with the scored results will appear
    4. Hover your cursor to the table
    5. Select the `Download as CSV` option
    6. Choose the location in which you wish to save the file
    7. Load the `.csv` in your preferred data analysis tool - spreadsheet or some other tool - and continue your data analysis process 
    """
)
