import json
from datetime import datetime, timedelta

class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, due_date):
        task = {
            'name': name,
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task['name']} - Due: {task['due_date']} {'(Completed)' if task['completed'] else ['Not completed']}")
            

    def upcoming_due_dates(self, days=7):
        upcoming_tasks = [task for task in self.tasks if not task['completed'] and
                          datetime.strptime(task['due_date'], '%Y-%m-%d') <= datetime.now() + timedelta(days=days)]
        return upcoming_tasks

# Example Usage
if __name__ == "__main__":
    tracker = TaskTracker()

    tracker.add_task("Laundry", "Wash neat and clean", "2022-01-01")
    tracker.add_task("Go shopping", "Grocery shopping", "2022-01-10")
    tracker.add_task("Research","Technolgy and AI","2022-01-13")
    tracker.add_task("Book flight tickets","To USA","2022-01-16")

    

    tracker.mark_completed(0)

    print("All Tasks:")
    tracker.list_tasks()

    print("\nUpcoming Due Dates:")
    upcoming_tasks = tracker.upcoming_due_dates()
    tracker.list_tasks()  # Display upcoming tasks

    # Save tasks to a file or database for persistence
    with open('tasks.json', 'w') as file:
        json.dump(tracker.tasks, file)
