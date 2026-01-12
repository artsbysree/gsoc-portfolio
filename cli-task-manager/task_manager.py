from storage import load_tasks, save_tasks


def add_task(description):
    tasks = load_tasks()
    tasks.append({
        "description": description,
        "completed": False
    })
    save_tasks(tasks)


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['description']} [{status}]")

from storage import load_tasks, save_tasks

def add_task(description):
    tasks = load_tasks()
    tasks.append({
        "description": description,
        "completed": False
    })
    save_tasks(tasks)

def get_tasks():
    return load_tasks()

def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        return True
    return False

