# does the same as todolist, but it identical to Ardit's code
# from functions import get_todos, write_todos

import functions
import time

while True:
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print("Is is", now)
    user_action = input("Add, show, edit, complete, or exit Todo list: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todo = todo + '\n'

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip()
            print(f"{index + 1}.{item}")

    elif user_action.startswith('edit'):

        todos = functions.get_todos()

        try:
            number = int(user_action[5:])
            number = number - 1
            print("current todo: ", todos[number])
            todos[number] = input("Enter new todo: ") + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid. Please enter edit with the number of the todo.")
            continue

    elif user_action.startswith('complete'):
        todos = functions.get_todos()
        try:
            number = int(user_action[9:])
            index = number - 1
            removed_todo = todos[index].strip()
            todos.pop(index)

            functions.write_todos(todos)

            print(f"You have completed: {removed_todo}")
        except IndexError:
            print("There is no todo with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")
print("Bye!")
