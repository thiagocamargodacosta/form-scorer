import streamlit as st
import pandas
import time

import scorer.dass as dass

# I like my tabs to have nice names...
st.set_page_config(
    page_title="Form scorer - DASS-21",
)

st.markdown("# Depression, Anxiety and Stress Scale (DASS-21)")

st.markdown(
    """
    **This tool was built to specifically support the data format that is produced by the Google Form for this questionnaire.**

    **Submissions that do not follow the format will fail to produce a result.**
    """
)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    dataframe = pandas.read_csv(uploaded_file)
    headers = list(dataframe.columns)

    if headers == dass.DASS_21_HEADERS:
        forms = list(dataframe.values)

        with st.spinner(text="Scoring in progress..."):
            time.sleep(1)
            result = dass.score(forms)
            st.success("Done!")
            st.markdown("## Scoring results")
            st.write(result)

    else:
        st.markdown("File does not match expected headers")
