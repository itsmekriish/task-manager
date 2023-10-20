# project.py

# Function to add a task
def add_task(tasks, title, description):
    task = {"title": title, "description": description, "complete": False}
    tasks.append(task)
    return tasks

# Function to view tasks
def view_tasks(tasks, filter_incomplete=True):
    filtered_tasks = [task for task in tasks if not filter_incomplete or not task["complete"]]
    return filtered_tasks

# Function to mark a task as complete
def mark_task_complete(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["complete"] = True
    return tasks

# Main function
def main():
    tasks = []  # Initialize an empty list to store tasks
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            tasks = add_task(tasks, title, description)
            print("Task added successfully!")

        elif choice == "2":
            tasks_to_view = view_tasks(tasks)
            print("\nAll Tasks:")
            for index, task in enumerate(tasks_to_view, start=1):
                status = "Complete" if task["complete"] else "Incomplete"
                print(f"{index}. {task['title']} ({status})")

        elif choice == "3":
            try:
                task_index = int(input("Enter the task number to mark as complete: ")) - 1
                tasks = mark_task_complete(tasks, task_index)
                print("Task marked as complete!")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
