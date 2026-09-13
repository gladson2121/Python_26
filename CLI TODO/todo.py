import time

welcome_message = "Welcome to the TODO APP!"

# Database to store the tasks.
# Structure: {task_id: {"title": str, "description": str, "status": str}}
datasource = {}
task_id_counter = 1


def add_task():
    global task_id_counter

    task_id = task_id_counter
    task_id_counter += 1
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    datasource[task_id] = {
        "title": title,
        "description": description,
        "status": "new",
    }


def view_task():
    if not datasource:
        print("No tasks found.")
        return

    for task_id, task in datasource.items():
        print(
            f"Task ID: {task_id}, Title: {task['title']}, "
            f"Description: {task['description']}, Status: {task['status']}"
        )
    time.sleep(2)


def complete_task():
    view_task()
    task_id = int(input("Enter the task ID to mark as complete: "))

    if task_id in datasource:
        datasource[task_id]["status"] = "Complete"
        print("Task marked as complete")
    else:
        print("Invalid task ID. Please try again.")
    time.sleep(2)


def update_task():
    view_task()
    task_id = int(input("Enter the task ID to update: "))

    if task_id in datasource:
        title = input("Enter the new title of the task:")
        description = input("Enter the new description of the task:")
        status = input("Enter the new status of the task:")
        backup_task = datasource[task_id]

        title = title if title else backup_task["title"]
        description = description if description else backup_task["description"]
        status = status if status else backup_task["status"]
        datasource[task_id] = {
            "title": title,
            "description": description,
            "status": status,
        }
        print("Task updated successfully.")
    else:
        print("Invalid task ID. Please try again.")
    time.sleep(2)


def delete_task():
    view_task()
    task_id = int(input("Enter the task ID to delete: "))

    if task_id in datasource:
        del datasource[task_id]
        print("Task deleted successfully.")
    else:
        print("Invalid task ID. Please try again.")
    time.sleep(2)


selection = """
1. Add Task
2. View Task
3. Update Task
4. Delete Task
5. Complete Task
6. Exit
"""
user_selection = 0

# Program starts here.
print(welcome_message)
while user_selection != 6:
    print(selection)
    user_selection = int(input("Enter your choice: "))

    match user_selection:
        case 1:
            add_task()
        case 2:
            view_task()
        case 3:
            update_task()
        case 4:
            delete_task()
        case 5:
            complete_task()
        case 6:
            print("Exiting the TODO APP")
        case _:
            print("Invalid selection. Please try again.")
