
import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List Application")

# Initialize the to-do list
todo_list = []

# Function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in todo_list:
        listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        todo_list.append(task)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to remove a task
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        todo_list.pop(selected_task_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Function to clear all tasks
def clear_tasks():
    global todo_list
    todo_list = []
    update_listbox()

# Creating the GUI components
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10, bd=0)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", width=48, command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=48, command=clear_tasks)
clear_button.pack(pady=5)

# Start the main loop
root.mainloop()
