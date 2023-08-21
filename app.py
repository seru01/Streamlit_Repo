import streamlit as st
st.title("Log in Form")
userName = st.text_input("USER NAME")
password = st.text_input("PASSWORD", type="password")
if st.button("SUBMIT"):
    if userName == "rey" and password =="rey123":
        st.write("username password correct !!! ")
    else:
        st.write("username or password incorrect!!!")
