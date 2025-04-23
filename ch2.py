import streamlit as st 

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your Chai  is being Brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("masala added your chai")

tea_type = st.radio("Pick Your Chai  Base :- ",["Milk","Water","Honey"])

st.write(f"selected base {tea_type}")

flavors = st.selectbox("Choose Flavor ",["Adrak","Kesar","Tulsi"])
st.write(f"selected flavor {flavors}")

sugar = st.slider("Sugar Level ", 0,5,2)
st.write(f"Sugar spoon {sugar}")

cups = st.number_input("How Many Cups :- ",min_value=1, max_value=10,step=1)
st.write(f"selected suger level {cups}")

name = st.text_input("Enter Your Name :- ")
if name:
    st.write(f"Welcome {name} ! your chai is on the way")

db = st.date_input("Select your date of birth")
st.write(f"you datec of birsth is {db}")
