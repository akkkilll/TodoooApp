from functions import getTodos, writeTodos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

print("To-Do List App: Add/Edit/Mark as Complete")

#   todos = []

prompt0 = "What action would you like to perform: "
prompt1 = "Enter a task to add: "

while True:
    action = (input(prompt0).strip())

    if action.startswith('add'):
        todo = action[4:] + "\n"
        
        todos = getTodos()
        todos.append(todo)
        
        writeTodos(todos)
                
    elif action.startswith('show'):
        todos = getTodos()
        # print_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}. {item}")
        
    elif action.startswith('edit'):
        try:
            index = int(action[5]) - 1

            todos = getTodos()

            existing_task = todos[index]
            new_task =  input("Enter task to replace/edit: ")
            todos[index] = new_task + '\n'
            
            writeTodos(todos)
                
            print("Task edited successfully!")
        
        except ValueError:
            print("Invalid command! Mention the INDEX NUMBER of the task you want to edit")
            continue

    elif action.startswith('exit'):
        print("Bye..")
        break

    elif action.startswith('complete'):
        try:
            index = int(action[9:])- 1

            todos = getTodos()

            todos.pop(index) 
        
            writeTodos(todos)
            
            print("Task marked as completed!!!")

        except IndexError:
            print("There is no item with that index number")
            continue

    else:
        print("Invalid command: try add/show/edit/complete/exit")


