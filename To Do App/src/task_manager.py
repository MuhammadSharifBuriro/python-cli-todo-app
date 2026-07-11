def add_task(tasks):
    task = input("Enter Task: ")

    tasks.append({
        "title": task,
        "completed": False
    })

    print("Task Added Succesfully! ")

def view_task(tasks):

    if len(tasks) == 0:
        print("No Task Available")
        return
    
    print("\n---------Tasks-----------")

    for index,task in enumerate(tasks,start = 1):
        status = "✓" if task["completed"]else  "✗"

        print(
            f"{index}.[{status}] {task['title']}"
        )

def complete_task(tasks):

    view_task(tasks)

    if len(tasks) == 0:
        return

    try:
        choice = int(input("Enter Task Number to Complete: "))

        task = tasks[choice - 1]

        task["completed"] = True

        print(f"{task['title']} Completed Successfully!")

    except (ValueError, IndexError):
        print("Invalid Task Number")
        
def delete_task(tasks):

    view_task(tasks)

    if len(tasks)== 0:
        return
    
    try:
        choice = int(input("Enter Task to delete: "))

        removed_task = tasks.pop(choice -1)

        print(f"{removed_task['title']} Deleted Succesfully! ")
    
    except (ValueError,IndexError):
        print("Invalid Task Number")