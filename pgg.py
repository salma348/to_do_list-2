import tkinter as tk
from tkinter import messagebox
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.task_name_entry = tk.Entry(self.root, width=40, font=("Helvetica", 14), bd=2, relief="flat")
        self.task_name_entry.pack(pady=10)
        self.task_name_entry.insert(0, "Enter task name")
        self.task_name_entry.bind("<FocusIn>", self.clear_task_name_placeholder)
        self.task_description_entry = tk.Entry(self.root, width=40, font=("Helvetica", 14), bd=2, relief="flat")
        self.task_description_entry.pack(pady=10)
        self.task_description_entry.insert(0, "Enter task description")
        self.task_description_entry.bind("<FocusIn>", self.clear_task_description_placeholder)
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task,
                                    bg="#00bfa5", fg="white", font=("Helvetica", 12, "bold"),
                                    relief="flat", padx=10, pady=5,
                                    activebackground="#009688", activeforeground="white")
        self.add_button.pack(pady=5)
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, bg="#f8f9fa", fg="#333", font=("Helvetica", 12),
                                       selectbackground="#00bfa5", selectforeground="white", bd=0, highlightthickness=1,
                                       highlightbackground="#d1d1d1", relief="flat")
        self.task_listbox.pack(pady=10)
        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task,
                                         bg="#00bfa5", fg="white", font=("Helvetica", 12, "bold"),
                                         relief="flat", padx=10, pady=5,
                                         activebackground="#009688", activeforeground="white")
        self.complete_button.pack(pady=5)
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task,
                                       bg="#00bfa5", fg="white", font=("Helvetica", 12, "bold"),
                                       relief="flat", padx=10, pady=5,
                                       activebackground="#009688", activeforeground="white")
        self.delete_button.pack(pady=5)

    def clear_task_name_placeholder(self, event):
        if self.task_name_entry.get() == "Enter task name":
            self.task_name_entry.delete(0, tk.END)

    def clear_task_description_placeholder(self, event):
        if self.task_description_entry.get() == "Enter task description":
            self.task_description_entry.delete(0, tk.END)

    def add_task(self):
        task_name = self.task_name_entry.get()
        task_description = self.task_description_entry.get()
        if task_name and task_description and task_name != "Enter task name" and task_description != "Enter task description":
            task = f"{task_name}: {task_description}"
            self.tasks.append({"name": task_name, "description": task_description, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_name_entry.delete(0, tk.END)
            self.task_description_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter both a task name and description.")

    def complete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            task = self.tasks[task_index]
            task["completed"] = True
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, f"{task['name']}: {task['description']} [Done]")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
