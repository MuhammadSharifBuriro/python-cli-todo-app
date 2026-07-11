from src.menu import show_menu

from src.task_manager import (
    add_task,
    view_task,
    complete_task,
    delete_task
)
from src.file_handler import (
    load_tasks,
    save_tasks
)

tasks = load_tasks()
print(tasks)

while True :
    choice = show_menu()

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_task(tasks)
    elif choice == "3":
        complete_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        save_tasks(tasks)
        print("\nTasks Saved Successfully!")
        print("Thank you for using ToDo App. Goodbye! 👋")
        break
    else:
        print("Invalid Choice")
