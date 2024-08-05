import streamlit as st
import functions

todos = functions.get_todos()

st.title("My To-do App")
st.subheader("This is my todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Enter a new todo")
