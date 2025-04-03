import tkinter as tk
from tkinter import simpledialog, messagebox

def task_manager_app():
    tasks = []  # List to store tasks

    # Function to add a task
    def add_task():
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            tasks.append(task.lower())
            update_task_list()
            messagebox.showinfo("Task Added", f"Task '{task}' has been added successfully!")

    # Function to update a task
    def update_task():
        if not tasks:
            messagebox.showwarning("No Tasks", "There are no tasks to update.")
            return
        try:
            index = int(simpledialog.askstring("Update Task", "Enter the task number to update:")) - 1
            if 0 <= index < len(tasks):
                new_task = simpledialog.askstring("New Task", "Enter the new task:")
                if new_task:
                    tasks[index] = new_task.lower()
                    update_task_list()
                    messagebox.showinfo("Task Updated", f"Task has been updated to '{new_task}'.")
            else:
                messagebox.showerror("Invalid Task Number", "The task number is not valid.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid task number.")

    # Function to delete a task
    def delete_task():
        if not tasks:
            messagebox.showwarning("No Tasks", "There are no tasks to delete.")
            return
        try:
            index = int(simpledialog.askstring("Delete Task", "Enter the task number to delete:")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                update_task_list()
                messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' has been deleted successfully!")
            else:
                messagebox.showerror("Invalid Task Number", "The task number is not valid.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid task number.")

    # Function to display tasks in the listbox
    def update_task_list():
        task_listbox.delete(0, tk.END)
        for idx, task in enumerate(tasks, start=1):
            task_listbox.insert(tk.END, f"{idx}. {task}")

    # Function to exit the program
    def exit_program():
        root.destroy()

    # Setting up the main window
    root = tk.Tk()
    root.title("Task Management App")

    tk.Label(root, text="Task Management App", font=("Helvetica", 16, "bold")).pack(pady=10)

    task_listbox = tk.Listbox(root, width=50, height=15)
    task_listbox.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack()

    tk.Button(button_frame, text="Add Task", width=15, command=add_task).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text="Update Task", width=15, command=update_task).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(button_frame, text="Delete Task", width=15, command=delete_task).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(button_frame, text="Exit", width=15, command=exit_program).grid(row=0, column=3, padx=5, pady=5)

    root.mainloop()

# Run the Task Management App
task_manager_app()
