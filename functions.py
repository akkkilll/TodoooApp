def getTodos(filepath='todos.txt'):
    """Returns the list of to-do items in the given file"""

    with open(filepath, 'r') as file:
        localtodos = file.readlines()
    return localtodos

def writeTodos(todos_arg, filepath='todos.txt'):
    """Write a to-do item list in the text file"""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)