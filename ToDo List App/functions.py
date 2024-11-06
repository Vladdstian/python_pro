def get_todos(filepath="todos.txt"):
    """
    Read a text file and return the list of To-Do items.
    :param filepath: string containing the path to the file used for saving the to-do-s
    :return: a list of To-Do items
    """
    with open(filepath, 'r') as f:
        local_todos = f.readlines()
    return local_todos


def write_todos(local_todos, filepath="todos.txt"):
    """
    Write the to-do items list in the text file.
    :param local_todos: provided list of to-do items
    :param filepath: string containing the path to the file used for saving the to-do-s
    :return: None
    """
    with open(filepath, 'w') as f:
        f.writelines(local_todos)
