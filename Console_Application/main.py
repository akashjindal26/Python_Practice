import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

while True:
    my_variable = input("Type Add, Show, Edit, Complete or Exit: ")
    my_variable = my_variable.strip()

    if my_variable.startswith("Add"):
        todo = my_variable[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif my_variable.startswith("Show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            output = f"{index+1}-{item}"
            print(output)

    elif my_variable.startswith("Edit"):
        try:
            number = int(my_variable[5:])
            number = number - 1
            update_todo = input("Enter new todo : ") + '\n'

            todos = functions.get_todos()

            todos[number] = update_todo

            functions.write_todos(todos)
        except ValueError:
            print("Please enter a valid command.")

    elif my_variable.startswith("Complete"):
        try:
            number = int(my_variable[9:])
            number = number - 1
            todos = functions.get_todos()

            if len(todos) <= number:
                todos.pop(number)

                functions.write_todos(todos)
            else:
                print("Out of list.")
        except ValueError:
            print("Please enter a valid command.")
    elif my_variable.startswith("Exit"):
        print("Exit")
    else:
        print("command is not valid.")
