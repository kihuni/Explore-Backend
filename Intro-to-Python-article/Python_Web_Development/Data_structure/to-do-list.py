# Define an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print("Task added successfully!")

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found in the to-do list.")

# Function to display the current to-do list
def display_todo_list():
    if len(todo_list) == 0:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Example usage
add_task("Buy groceries")
add_task("Finish homework")
add_task("Call mom")
display_todo_list()
remove_task("Finish homework")
display_todo_list()
