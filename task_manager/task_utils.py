from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

# Task structure:
# {"title": "", "description": "", "due_date": "", "completed": False}

def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title")
        return

    if not validate_task_description(description):
        print("Invalid description")
        return

    if not validate_due_date(due_date):
        print("Invalid due date format (YYYY-MM-DD)")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index")


def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]

    if not pending:
        print("No pending tasks")
        return

    for i, task in enumerate(pending, 1):
        print(f"{i}. {task['title']} - {task['due_date']}")


def calculate_progress():
    if not tasks:
        print("No tasks available")
        return

    completed = sum(1 for t in tasks if t["completed"])
    total = len(tasks)

    progress = (completed / total) * 100
    print(f"Progress: {progress:.2f}% ({completed}/{total})")