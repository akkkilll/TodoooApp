import streamlit as st
from functions import getTodos, writeTodos

todos = getTodos()

def addTodo():
    todo = st.session_state["newtodo"] + "\n"
    todos.append(todo)
    writeTodos(todos)

st.title("ToDooo..")
st.write("ToDooo web app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        writeTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun() #Try st.rerun() if error is diplayed

st.text_input(label=" ", placeholder="Add a new task", 
 on_change=addTodo, key="newtodo")