import streamlit as st
from datetime import date
 
st.title("Assignment")

db = st.date_input("Enter Your Date Of Birth :- ")

if db:
    today = date.today()

    age = today.year - db.year

    st.write(f"your age is {age}")