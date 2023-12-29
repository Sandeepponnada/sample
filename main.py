import streamlit as st
import numpy as np

st.set_page_config(layout ="wide")
st.title("Student Management System")
st.sidebar.title("Fee Management System")

st.sidebar.subheader("Menu")
radio_value = st.siderbar.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

