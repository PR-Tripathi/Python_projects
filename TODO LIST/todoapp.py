import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class TodoApp:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.load_todos()

        # Create the main window
        self.root = tk.Tk()
        self.root.title("To-Do App")
        self.root.configure(bg="#f0f0f0")  # Set initial background color

        # Create the listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Create buttons for CRUD operations with colors
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="#2196F3", fg="white", font=("Arial", 12))
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="#F44336", fg="white", font=("Arial", 12))
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed, bg="#FF9800", fg="white", font=("Arial", 12))
        self.complete_button.pack(pady=5)

        # Button to change background color
        self.change_bg_button = tk.Button(self.root, text="Change Background Color", command=self.change_bg_color, bg="#9C27B0", fg="white", font=("Arial", 12))
        self.change_bg_button.pack(pady=10)

        self.load_tasks_to_listbox()

        self.root.mainloop()

    def load_todos(self):
        """Load todos from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.todos = json.load(file)
        else:
            self.todos = []

    def save_todos(self):
        """Save todos to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.todos, file, indent=4)

    def load_tasks_to_listbox(self):
        """Load tasks into the listbox."""
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for todo in self.todos:
            status = "✓" if todo['completed'] else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {todo['task']}")

    def add_task(self):
        """Add a new task."""
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.todos.append({'task': task, 'completed': False})
            self.save_todos()
            self.load_tasks_to_listbox()

    def update_task(self):
        """Update an existing task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                self.todos[index]['task'] = new_task
                self.save_todos()
                self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        """Delete a task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.todos.pop(index)
            self.save_todos()
            self.load_tasks_to_listbox()
            messagebox.showinfo("Delete Task", f'Task "{removed_task["task"]}" deleted.')
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def mark_completed(self):
        """Mark a task as completed."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todos[index]['completed'] = True
            self.save_todos()
            self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Mark as Completed", "Please select a task to mark as completed.")

    def change_bg_color(self):
        """Change the background color of the window and all widgets."""
        new_color = "#e0f7fa"  # Set to the color of your choice
        self.root.configure(bg=new_color)  # Change window background color
        self.task_listbox.configure(bg=new_color)  # Change listbox background
        self.add_button.configure(bg="#4CAF50", fg="white")  # Set button color
        self.update_button.configure(bg="#2196F3", fg="white")
        self.delete_button.configure(bg="#F44336", fg="white")
        self.complete_button.configure(bg="#FF9800", fg="white")
        self.change_bg_button.configure(bg="#9C27B0", fg="white")  # Set button color

if __name__ == "__main__":
    TodoApp()
