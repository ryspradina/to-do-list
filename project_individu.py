import tkinter
from tkinter import *
import tkinter.messagebox
window = tkinter.Tk()
window.title("To-Do List")



def add_task():
    task = entry_button.get()
    if task != "":
        listbox_task.insert(END, task)
        entry_button.delete(0, END)
    else:
        tkinter.messagebox.showwarning(
            title="Warning!", message="You must enter a task.")
    

def delete_task():
    try:
        task_index = listbox_task.curselection()
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(
            title="Warning!", message="You must select a task.")


frame_tasks = tkinter.Frame(window)
frame_tasks.pack()


#BUTTON WIDGET
listbox_task = Listbox(frame_tasks, bg="black",fg="pink", height=20, width=50)
listbox_task.pack()

entry_button = Entry(window, width=50)
entry_button.pack()

add_task_button = Button(window, text='Add Task', width=48, command=add_task)
add_task_button.pack()

delete_task_button = Button (window, text="Delete Task", width=48, command=delete_task)
delete_task_button.pack()


window.mainloop()
