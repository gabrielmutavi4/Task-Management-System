from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

import json

# ---------- SAVE TASKS ----------
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# ---------- LOAD TASKS ----------
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# ---------- ADD TASK ----------
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# ---------- MARK COMPLETE ----------
def mark_task_as_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task index")


# ---------- DELETE TASK ----------
def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task index")


# ---------- VIEW PENDING ----------
def view_pending_tasks(tasks):
    pending = [t for t in tasks if not t["completed"]]

    if not pending:
        print("No pending tasks")
        return

    for task in pending:
        print(f"{task['title']} - {task['due_date']}")


# ---------- PROGRESS ----------
def calculate_progress(tasks):
    if len(tasks) == 0:
        print(0)
        return 0

    completed = 0

    for task in tasks:
        if task.get("completed") == True:
            completed += 1

    progress = (completed / len(tasks)) * 100
    return progress