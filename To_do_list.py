import os

FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return f.read().splitlines()

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        if not tasks:
            print("No tasks found")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added ✅")

    elif choice == '3':
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number")

    elif choice == '4':
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")