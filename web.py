import streamlit as st
import function

todos = function.get_Todos()
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    function.write_Todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_Todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter Todo:", placeholder="Add new Todo...",
              on_change=add_todo, key='new_todo')