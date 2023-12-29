import streamlit as st
st.set_page_config(layout="wide")
st.tittle("student management System")
st.sidebar.tittle("free managemnet  System")
st.sidebar.subheader("Add student")
name=st.sidebar.text_input("name")
fees= st.sidebar.text_input("amount")
add=t.sidebar.button("ADD")
