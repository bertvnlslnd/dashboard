import streamlit as st

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
             #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
