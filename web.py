import streamlit as st
from functions import getTodos, writeTodos

st.title("ToDooo..")
st.write("ToDooo web app")

todos = getTodos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new task")