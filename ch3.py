import streamlit as st 

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs3tJusx9oiBdPVz7UpmsZ8vE3YkWyZDCiyA&s",width=500)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://www.teacupsfull.com/cdn/shop/articles/Screenshot_2023-10-20_at_11.07.13_AM.png?v=1697780292",width=500)
    vote2 = st.button("Vote Adrak Chai")

if  vote1:
    st.success("Thanks  For Voting Masala Chai")
elif vote2:
    st.success("Thanks  For Voting Adrak Chai")

name = st.sidebar.text_input("Enter Your name")
tea = st.sidebar.selectbox("choose your chai",["masala","kesar","adrak"])

st.write(f"welcome {name} your {tea} chai is getting ready")

with st.expander("Show Chai making instruction"):
    st.write("""
        1. boil water with tea  lives.
        2. add milk and spices.
        3. serve hot
    """)

st.markdown('## Welcome to chai app')
st.markdown('> markdown')