import json
import time

welcome_message = "Welcome to the TODO APP!"

# Database to store the tasks.
# Structure: {task_id: {"title": str, "description": str, "status": str}}
datasource = {}
task_id_counter = 1
status_options = ["New", "In Progress", "Complete"]

#loading existing tasks from the JSON file if it exists
try:
    with open("D:\\Dev\\Python\\Basics\\Python_26\\CLI TODO\\data\\todo.json", "r") as f:
        datasource = json.load(f)
        if datasource:
            task_id_counter = int(max(datasource.keys())) + 1
except FileNotFoundError:
    pass


json_file_path = "D:\\Dev\\Python\\Basics\\Python_26\\CLI TODO\\data\\todo.json"
def add_task():
    global task_id_counter

    task_id = task_id_counter
    
    while True:
        title = input("Enter the title of the task: ")
        if title:
            break
        print("Title cannot be empty. Please enter a valid title.")
    
    while True:
        description = input("Enter the description of the task: ")
        if description:
            break
        print("Description cannot be empty. Please enter a valid description.")
    status = input("Enter the status of the task (New, In Progress, Complete): ")
    # Validate the status input
    while status not in status_options:
        print("Invalid status. Please enter a valid status (New, In Progress, Complete).")
        status = input("Enter the status of the task (New, In Progress, Complete): ")
    datasource[task_id] = {
        "title": title,
        "description": description,
        "status": status,
    }
    task_id_counter += 1


def view_task():
    if not datasource:
        print("No tasks found.")
        return

    for task_id, task in datasource.items():
        print(
            f"Task ID: {task_id}, Title: {task['title']}, "
            f"Description: {task['description']}, Status: {task['status']}"
        )
    


def complete_task():
    view_task()
    task_id =input("Enter the task ID to mark as complete: ") 
    if task_id in datasource:
        datasource[task_id]["status"] = "Complete"
        print("Task marked as complete")
    else:
        print("Invalid task ID. Please try again.")
    time.sleep(2)


def update_task():
    view_task()
    time.sleep(2)

    task_id = input("Enter the task ID to update: ")
   
    if task_id in datasource:
        title = input("Enter the new title of the task:")
        description = input("Enter the new description of the task:")
        status = input("Enter the new status of the task (New, In Progress, Complete): ")
        if status != "":
            while (status not in status_options):
                print("Invalid status. Please enter a valid status (New, In Progress, Complete).")
                status = input("Enter the status of the task (New, In Progress, Complete): ")
            

    
        datasource[task_id]["title"]= title if title else datasource[task_id]["title"]     
        datasource[task_id]["description"] = description if description else datasource[task_id]["description"]
        datasource[task_id]["status"] = status if status else datasource[task_id]["status"]
        print("Task updated successfully.")
    else:
        print("Invalid task ID. Please try again.")
    time.sleep(2)


def delete_task():
    view_task()
    time.sleep(2)
    task_id = input("Enter the task ID to delete: ")
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
    json_file = json.dumps(datasource)
    print(selection)
    try:
        user_selection = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

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
            
json_file = json.dumps(datasource)
with open(json_file_path, "w") as f:
    f.write(json_file)

