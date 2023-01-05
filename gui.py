from functions import getTodos, writeTodos
import time
import PySimpleGUI as sg

sg.theme("DarkBlue")

clock = sg.Text("", key="clock")
label = sg.Text("Task to add:")
inputBox = sg.InputText(tooltip = "Enter task", key='todo', size=[32,4])
addButton = sg.Button("Add")

listbox = sg.Listbox(values=getTodos(), key='existingtodo',
 enable_events=True, size=[30,10])

editButton = sg.Button("Edit")
completebutton = sg.Button("Complete")
exitbutton = sg.Button("Exit")

#Create Instance
window = sg.Window('ToDooo App',
    layout = [[clock],
     [label],
      [inputBox, addButton],
       [listbox, editButton, completebutton],
        [exitbutton]],
    font=('Helvetica', 13))

while True:
    event, values = window.read(timeout=200)   #Displays the window and reads user input
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S  -  ToDooo App"))

    match event:
        case "Add": 
            todos = getTodos()
            newtodo = values['todo'] + "\n"   #Stores the value of todo key in the dictionary
            todos.append(newtodo)
            writeTodos(todos)

            window['existingtodo'].update(values=todos)
            window['todo'].update(value="")
        
        case "Edit":
            try:
                todos = getTodos()
                newtodo = values['todo'] + "\n"
                selectedtodo = values['existingtodo'][0]

                index = todos.index(selectedtodo)
                todos[index] = newtodo
                writeTodos(todos)

                window['existingtodo'].update(values=todos)
            
            except IndexError:
                sg.popup("Select a task for editing..", font=("Helvetica", 15))


        case "Complete":
            try:
                completetodo = values['existingtodo'][0]
                todos = getTodos()
                todos.remove(completetodo)
                writeTodos(todos)
                window['existingtodo'].update(values=todos)
                window['todo'].update(value="")

            except IndexError:
                sg.popup("Choose a task to mark as complete", font=("Helvetica", 15))

        
        case "existingtodo":
            window['todo'].update(value = values['existingtodo'][0])
        
        case "Exit":
            break

        case sg.WIN_CLOSED:
            break


window.close()  #Closes the window