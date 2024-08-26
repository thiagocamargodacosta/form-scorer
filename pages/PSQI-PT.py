import streamlit as st
import pandas
import time

import scorer.psqi as psqi

# I like my tabs to have nice names...
st.set_page_config(
    page_title="Form scorer - PSQI-PT",
)

st.markdown("# Pittsburgh Sleep Quality Index (Portuguese version)")

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

    if headers == psqi.PSQI_HEADERS:
        forms = list(dataframe.values)
        with st.spinner(text="Scoring in progress..."):
            time.sleep(1)
            result = psqi.score(forms)
            st.success("Done!")
            st.markdown("## Scoring results")
            st.write(result)
    else:
        st.markdown("File does not match expected headers")
