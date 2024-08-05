import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt" , 'w') as file:
        pass

now = time.strftime("%b %d, %Y")
sg.theme("DarkBlue")

clock = sg.Text(f"{now}", key='clock')
label = sg.Text("Type in a to-do")

input_box = sg.InputText(tooltip="Enter todo", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))

add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete", button_color="Green")
exit_button = sg.Button("Exit", button_color="Red")

window = sg.Window('My To-DO Ap',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box],
                           [edit_button, complete_button, exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                new_todo = new_todo.strip()

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)

                todos[index] = new_todo + '\n'
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                complete_todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(complete_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Exit":
            window.close()

        case "todos":
            window["todo"].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
