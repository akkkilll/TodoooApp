from functions import getTodos, writeTodos
import time
import PySimpleGUI as sg

label = sg.Text("Task to add:")
inputBox = sg.InputText(tooltip = "Enter task")

print("Hello")

addButton = sg.Button("Add")

#Create Instance
window = sg.Window('ToDooo App', layout = [[label], [inputBox, addButton]])
window.read()   #Displays the window
window.close()  #Closes the window