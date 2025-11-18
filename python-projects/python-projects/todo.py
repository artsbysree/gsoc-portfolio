# Simple To-Do App by Sree Divya 🌸

tasks = []

def show_menu():
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"✔️ '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet! 🌸")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"❌ '{removed}' removed!")
    except (ValueError, IndexError):
        print("Invalid choice.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Bye! Have a productive day 🌿")
        break
    else:
        print("Invalid choice, try again.")
