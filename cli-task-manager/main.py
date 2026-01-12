from task_manager import add_task, get_tasks, complete_task


def show_menu():
    print("\n==== CLI Task Manager ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        # ✅ Add Task
        if choice == "1":
            task_desc = input("Enter task description: ")
            add_task(task_desc)
            print("Task added ✅")

        # ✅ View Tasks
        elif choice == "2":
            tasks = get_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, start=1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. {task['description']} [{status}]")

        # ✅ Mark Task as Completed
        elif choice == "3":
            tasks = get_tasks()
            if not tasks:
                print("No tasks to complete.")
            else:
                for i, task in enumerate(tasks, start=1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. {task['description']} [{status}]")

                try:
                    task_num = int(input("Enter task number: "))
                    if complete_task(task_num - 1):
                        print("Task completed 🎉")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        # ✅ Exit
        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
