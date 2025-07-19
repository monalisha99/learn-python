import tkinter as tk
import tkinter.font as font


def delete_tasks(task_list):    # Clear the task list
    task_list.clear()

    # Remove all labels and checkboxes from the GUI
    for widget in root.grid_slaves():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Checkbutton):
            widget.grid_forget()

    # # Optionally, you can also clear the entry box
    # entry_box.delete(0, tk.END)
    
def addtask():
    # obtain the value from entry box
    value = entry_box.get()

    # store the entry value to a list
    task_list.append(value)
    # print('Entered Text:', task_list)

    # Loop through the task_list and display labels.
    for i in range(len(task_list)):
        task_label =tk.Label(root, text=f"{i+1}. "+ task_list[i])
        task_label.grid(row=1+i, column=0)

        # to display checkbox
        cb = tk.Checkbutton(root)
        cb.grid(row=1+i, column=1)


# create a list to store tasks
task_list = []


root = tk.Tk()

root.title('To Do List')
root.geometry('640x480')

# Add Widgets here, we will use .pack() method
entry_box = tk.Entry(root, width=60)
entry_box.grid(row=0, column=0)

# add button
add_button = tk.Button(root, text="Add", command=lambda:addtask())
add_button.grid(row=0, column=1)

# delete button
delete_button = tk.Button(root, text="Delete", command=lambda: delete_tasks(task_list))
delete_button.grid(row=0, column=2)


root.mainloop()
