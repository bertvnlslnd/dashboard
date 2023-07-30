import streamlit as st
import pandas as pd
import numpy as np
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title ("Eierenstatistiek")
# st.header("this is the markdown")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r''' a+a r^1+a r^2+a r^3 ''')
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)
st.caption("TIJD")
st.image("assets/test.jpg")

