from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks
)

def menu():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            add_task(title, desc, due)

        elif choice == "2":
            for i, t in enumerate(tasks):
                status = "✔" if t["completed"] else "❌"
                print(f"{i}. {t['title']} [{status}]")

            index = int(input("Enter task index: "))
            mark_task_as_complete(index)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

menu()