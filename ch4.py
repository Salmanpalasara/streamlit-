import streamlit as st 
import pandas as pd 

st.title("Chai Sales DashBoard")

file = st.file_uploader("upload your ccsv file",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("data preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    city = df["city"].unique()
    selected_city = st.selectbox("filter by cities", city)
    filtered_data = df[df["city"] == selected_city]
    st.dataframe(filtered_data)
