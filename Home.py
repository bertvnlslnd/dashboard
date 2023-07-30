import streamlit as st
import numpy as np
import time
st.set_page_config(page_title = "Vanelslande NV smart garden solutions")
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title ("Welkom in uw tuin")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")