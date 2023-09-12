filePath = "todos.txt"


def get_todos():
    with open(filePath, 'r') as content:
        todos_list = content.readlines()
    return todos_list


def write_todos(todos_list):
    with open(filePath, 'w') as content:
        content.writelines(todos_list)