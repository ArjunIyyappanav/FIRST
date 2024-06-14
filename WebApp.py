import streamlit as st
from functionsweb import get,writetodo,complete

# with open('todos.txt','w') as file:
#     file.write("Running\n")
#     file.write("Get Grocery\n")
#     file.write("Take out the Garbage\n")
# #while True:

def Add_todo():
    value = st.session_state["Newtodo"]
    print(type(value))
    writetodo(value+'\n')


def Complete_todo():
    content = get()
    for i in st.session_state:
        if st.session_state[i] == True:
            content.pop(int(i)-1)
            with open("todos.txt",'w') as file:
                file.writelines(content)
            del st.session_state[i] 
            
st.title("My to-do App")
content = get()

for no,task in enumerate(content):
    st.checkbox(task.strip('\n'),on_change = Complete_todo,key = no+1)
st.text_input(label="",placeholder = "Enter a todo",on_change = Add_todo,key = "Newtodo")