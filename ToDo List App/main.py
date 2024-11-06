from functions import get_todos, write_todos

while True:
    user_action = input("Type add, edit, complete, show or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item.capitalize()}")

    elif user_action.startswith('edit'):
        try:
            item_index = int(user_action[5:])
            item_index -= 1
            todos = get_todos()
            new_todo = input("Enter new ToDo: ")
            todos[item_index] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith('complete'):
        try:
            item_index = int(user_action[9:])
            todos = get_todos()
            removed_todo = todos.pop(item_index - 1).strip('\n')
            write_todos(todos)
            print(f"Todo '{removed_todo}' was removed  from the list.")
        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("You have entered an invalid command!")


print("Bye!")
