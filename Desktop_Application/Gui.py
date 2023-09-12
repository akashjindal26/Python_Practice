import functions
import PySimpleGUI as Sg
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

label = Sg.Text("Todos List")
input_textBox = Sg.InputText(tooltip="Enter Todo", key="addTodos")
add_button = Sg.Button("Add")

list_box = Sg.Listbox(tooltip="Todos list",
                      values=functions.get_todos(),
                      key="todosList",
                      enable_events=True,
                      size=(45, 10))

edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window(title="My Todos List",
                   layout=[[label],
                           [input_textBox, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Verdana", 15))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["addTodos"]
            todos.append(new_todo + '\n')
            functions.write_todos(todos)
            window["addTodos"].update("")
            window['todosList'].update(todos)
        case "Edit":
            try:
                edit_todo = values["todosList"][0]
                todos = functions.get_todos()
                index = todos.index(edit_todo)
                new_todo = values["addTodos"] + '\n'
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todosList'].update(todos)
                window["addTodos"].update("")
            except IndexError:
                Sg.popup("Please select an item.")
        case "Complete":
            try:
                complete_todo = values["todosList"][0]
                todos = functions.get_todos()
                index = todos.index(complete_todo)
                todos.pop(index)
                functions.write_todos(todos)
                window['todosList'].update(todos)
                window["addTodos"].update("")
            except IndexError:
                Sg.popup("Please select an item.")
        case "Exit":
            exit()
        case "todosList":
            window["addTodos"].update(values["todosList"][0])

        case Sg.WINDOW_CLOSED:
            break

window.close()
