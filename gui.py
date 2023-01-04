from functions import getTodos, writeTodos
import time
import PySimpleGUI as sg

label = sg.Text("Task to add:")
inputBox = sg.InputText(tooltip = "Enter task", key='todo')

addButton = sg.Button("Add")

#Create Instance
window = sg.Window('ToDooo App',
    layout = [[label], [inputBox, addButton]],
    font=('Helvetica', 13))

while True:
    event, values = window.read()   #Displays the window and reads user input

    match event:
        case "Add": 
            todos = getTodos()
            newtodo = values['todo'] + "\n"   #Stores the value of todo key in the dictionary
            todos.append(newtodo)
            writeTodos(todos)
        
        case sg.WIN_CLOSED:
            break


window.close()  #Closes the window