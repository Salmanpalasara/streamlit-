import streamlit as st 
import requests

st.title("Live Currency Converter")

amount = st.number_input("Enter The Amount in INR",min_value=1)

targetcurrency = st.selectbox("Convert To :- ",["USD","EUR","GBP","JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"

    response = requests.get(url)

    if response.status_code == 200:
       data = response.json()
       rate = data["rates"][targetcurrency] 
       converted = rate * amount

       st.success(f"{amount} INR = {converted:.2f} {targetcurrency}")
    else:
        st.error("Failed to conversion raate")