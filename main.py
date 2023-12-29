import streamlit as st

#st.write("<h1>Hello Priya</h1>",unsafe_allow_html=True)

#apply style
#st.write("<h1 style='color:blue;'>Hello Priya</h1>",unsafe_allow_html=True)

#upload file
#st.file_uploader("upload file")

#upload image
#st.image("https://img.freepik.com/free-photo/beautiful-rose-nature_23-2150737339.jpg")

#upload video
#st.video("https://www.youtube.com/watch?v=DBlMnnuVBO4")

#taking an image as input and displaying it
#img=st.file_uploader("upload image")
#st.image(img)
st.set_page_config(layout="wide")
st.tittle("student management System")
st.sidebar.tittle("free managemnet  System")
st.sidebar.subheader("Add student")
name=st.sidebar.text_input("name")
fees= st.sidebar.text_input("amount")
add=t.sidebar.button("ADD")
