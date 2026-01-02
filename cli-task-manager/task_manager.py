from storage import load_tasks, save_tasks

def add_task():
    task = input("Enter a new task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def main():
    print("CLI Task Manager")
    print("1. Add Task")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
