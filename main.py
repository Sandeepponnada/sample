import streamlit as st
import numpy as np

st.set_page_config(layout ="wide")
st.title("Student Management System")
st.sidebar.title("Fee Management System")
st.siderbar.color("black")

st.sidebar.subheader("Menu")
radio_value = st.sidebar.radio("Choose an option:", ["add student", "delete student", "view fee","pay fee"])
st.write("You selected:", radio_value)
if radio_value =="add student":
  rollnumber=st.text_input("Enter student number")
  name=st.text_input("Name")
  fees=st.number_input("Fees")
  add=st.button("Add Student")
elif radio_value == "delete student":
  rollnumber=st.text_input("Enter student number")
  name=st.text_input("enter Name")
  delete=st.button("delete record")
elif radio_value =="view fee":
  rollnumber=st.text_input("Enter student number")
  name=st.text_input("enter Name")
  view=st.button("view fee")
elif radio_value=="pay fee":
  rollnumber=st.text_input("Enter student number")
  name=st.text_input("Enter Name")
  fee=st.number_input("enter amount")
  Pay=st.button("Pay")

