import streamlit as st

# code to hide the watermark using CSS

# #MainMenu to hide the burger menu at the top-right side
# footer to hide the ```made with streamlit``` mark
hide = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide, unsafe_allow_html=True)

st.header("Hide the burger menu and watermark")