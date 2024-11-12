import json

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, description):
        task = {"description": description, "status": "Incomplete"}
        self.tasks.append(task)
        print(f'Task "{description}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['description']} - {task['status']}")

    def mark_as_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["status"] = "Done"
            print(f'Task "{self.tasks[task_index - 1]["description"]}" marked as Done.')
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f'Task "{deleted_task["description"]}" deleted successfully.')
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
        print(f'To-Do List saved to {filename}.')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            print(f'To-Do List loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found.')

# Example Usage:
todo_list = ToDoList()

while True:
    print("\n==== To-Do List Application ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Quit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        description = input("Enter task description: ")
        todo_list.add_task(description)
    elif choice == '2':
        todo_list.view_tasks()
    elif choice == '3':
        task_index = int(input("Enter the task index to mark as done: "))
        todo_list.mark_as_done(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task index to delete: "))
        todo_list.delete_task(task_index)
    elif choice == '5':
        filename = input("Enter the filename to save the to-do list: ")
        todo_list.save_to_file(filename)
    elif choice == '6':
        filename = input("Enter the filename to load the to-do list: ")
        todo_list.load_from_file(filename)
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")