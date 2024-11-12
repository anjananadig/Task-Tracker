# Task-Tracker

A simple Python application to help manage tasks, mark them as completed, and check for upcoming due dates. This project uses basic functionality to add, view, and complete tasks, making it ideal for beginners to practice with Python classes and file operations.

Features
Add Tasks: Create a task with a name, description, and due date.
Mark Tasks as Completed: Update a task’s status to completed.
List Tasks: View all tasks with their due dates and completion status.
View Upcoming Tasks: Filter tasks that are due within a specified number of days (default is 7).
Save Tasks: Save all tasks to a JSON file for persistence.
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/TaskTracker.git
Change to the project directory:
bash
Copy code
cd TaskTracker
Ensure you have Python 3 installed. Install any dependencies if necessary.
Usage
Run the script in a Python environment to interact with TaskTracker.

bash
Copy code
python task_tracker.py
Example Usage
Add a new task with a name, description, and due date.
Mark a task as completed by index.
List all tasks with status.
Check upcoming tasks within the next 7 days (default).
Saving Tasks
All tasks are automatically saved to a tasks.json file for persistence. Reloading from the file would require additional code to load tasks on start-up.

File Structure
task_tracker.py: The main file containing the TaskTracker class and task operations.
tasks.json: The JSON file where tasks are saved for persistence.
Contributing
Feel free to fork this repository, make improvements, and submit a pull request.

