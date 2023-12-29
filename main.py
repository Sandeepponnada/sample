import streamlit as st
import numpy as np

st.set_page_config(layout ="wide")
st.title("Student Management System")
st.sidebar.title("Fee Management System")

st.sidebar.subheader("Menu")
st.siderbar.radio("Choose an option:",["Add student","delete student","view fee","pay fee"])
