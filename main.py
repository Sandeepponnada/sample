import streamlit as st
import numpy as np

st.set_page_config(layout ="wide")
st.title("Student Management System")
st.sidebar.title("Fee Management System")

st.sidebar.subheader("Menu")
st.sidebar.subheader("choose an option")
st.siderbar.radio("Add student","delete student","view fee","pay fee")
