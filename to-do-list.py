

import tkinter as tk
from tkinter import messagebox

# function to add task

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
        
        
 # function to delete task       
def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks_listbox.delete(selected[0])
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
   
# main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")


# Title label
tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold")).pack(pady=10)

# Entry widget to enter tasks
task_entry = tk.Entry(root, width=25, font=("Arial", 12))
task_entry.pack(pady=10)

# Add Task button
add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

# Listbox to show tasks
tasks_listbox = tk.Listbox(root, width=30, height=10, font=("Arial", 12))
tasks_listbox.pack(pady=10)

# Delete Task button
del_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
del_btn.pack(pady=5)

# Run the app
root.mainloop()







