from functions import getTodos, writeTodos
import time
import PySimpleGUI as sg

label = sg.Text("Task to add:")
inputBox = sg.InputText(tooltip = "Enter task", key='todo')
addButton = sg.Button("Add")

listbox = sg.Listbox(values=getTodos(), key='existingtodo',
 enable_events=True, size=[30,10])

editButton = sg.Button("Edit")
completebutton = sg.Button("Complete")
exitbutton = sg.Button("Exit")

#Create Instance
window = sg.Window('ToDooo App',
    layout = [[label],
     [inputBox, addButton],
      [listbox, editButton, completebutton],
       [exitbutton]],
    font=('Helvetica', 13))

while True:
    event, values = window.read()   #Displays the window and reads user input

    match event:
        case "Add": 
            todos = getTodos()
            newtodo = values['todo'] + "\n"   #Stores the value of todo key in the dictionary
            todos.append(newtodo)
            writeTodos(todos)

            window['existingtodo'].update(values=todos)
        
        case "Edit":
            todos = getTodos()
            newtodo = values['todo'] + "\n"
            selectedtodo = values['existingtodo'][0]

            index = todos.index(selectedtodo)
            todos[index] = newtodo
            writeTodos(todos)

            window['existingtodo'].update(values=todos)

        case "Complete":
            completetodo = values['existingtodo'][0]
            todos = getTodos()
            todos.remove(completetodo)
            writeTodos(todos)
            window['existingtodo'].update(values=todos)
            window['todo'].update(value="")
        
        case "existingtodo":
            window['todo'].update(value = values['existingtodo'][0])
        
        case "Exit":
            break

        case sg.WIN_CLOSED:
            break


window.close()  #Closes the window