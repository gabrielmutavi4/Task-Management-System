from task_manager.task_utils import (
    load_tasks,
    add_task,
    mark_task_as_complete,
    delete_task,
    view_pending_tasks,
    calculate_progress
)

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = load_tasks()


while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. View Pending Tasks")
    print("4. Show Progress")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ---------- ADD TASK ----------
    if choice == "1":
        try:
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date: ")

            validate_task_title(title)
            validate_task_description(description)
            validate_due_date(due_date)

            task = {
                "title": title,
                "description": description,
                "due_date": due_date,
                "completed": False
            }

            add_task(tasks, task)

        except ValueError as e:
            print("Error:", e)


    # ---------- COMPLETE TASK ----------
    elif choice == "2":
        index = int(input("Enter task index: ")) - 1
        mark_task_as_complete(tasks, index)


    # ---------- VIEW PENDING ----------
    elif choice == "3":
        view_pending_tasks(tasks)


    # ---------- DELETE TASK ----------
    elif choice == "4":
        print(calculate_progress(tasks))


    # ---------- PROGRESS ----------
    elif choice == "5":
        print("Goodbye!")
        break


    # ---------- EXIT ----------
    elif choice == "6":
        print("Goodbye!")
        break


    else:
        print("Invalid choice")