import streamlit as st
import numpy as np 
import pandas as pd

st.title("hello chai app")
st.subheader("brewed with streamlit")
st.text("Welcome to first interative app")
st.write("choose your favrate chai")

chai = st.selectbox("your fav chai :- ",["masala chai","lemon chai","adrak chai","kesar chai"])

st.write(f"you choose {chai} it is a excellent chai")

st.success("your chai has been brewed")