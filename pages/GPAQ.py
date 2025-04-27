import streamlit as st
import pandas
import time

import scorer.gpaq as gpaq

st.set_page_config(
    page_title="Form Scorer - GPAQ"
)

st.markdown("# Global Physical Activity Questionnaire (GPAQ)")

st.markdown(
    """
    **This tool was built to specifically support the data format that is produced by the Google Form for this questionnaire.**

    **Submissions that do not follow the format will fail to produce a result.**
    """
)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    dataframe = pandas.read_csv(uploaded_file)
    headers   = list(dataframe.columns)
    st.markdown("## Forms table")
    st.write(dataframe)
    if headers == gpaq.GPAQ_HEADERS:
        forms = list(dataframe.values)

        with st.spinner(text="Scoring in progress..."):
            time.sleep(1)
            result = gpaq.score(forms)
            st.success("Done!")
            st.markdown("## Scoring results")
            st.write(result)
    
    else:
        st.markdown("File does not match expected headers")