import json
import os

# =========================
# CONFIG
# =========================
FILE_NAME = "tasks.json"


# =========================
# MODEL
# =========================
class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["done"])


# =========================
# STORAGE
# =========================
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return [Task.from_dict(t) for t in data]
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)


# =========================
# UI FUNCTIONS
# =========================
def show_menu():
    print("\n========== TASK MANAGER ==========")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Done" if task.done else "✖ Not Done"
        print(f"{i}. {task.title} [{status}]")


# =========================
# LOGIC
# =========================
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append(Task(title))
    save_tasks(tasks)
    print("Task added successfully!")


def delete_task(tasks):
    show_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed.title}")

        else:
            print("Invalid number!")

    except ValueError:
        print("Please enter a valid number!")


def mark_done(tasks):
    show_tasks(tasks)

    try:
        index = int(input("Enter task number to mark done: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index].done = True
            save_tasks(tasks)
            print("Task marked as done!")

        else:
            print("Invalid number!")

    except ValueError:
        print("Please enter a valid number!")


# =========================
# MAIN LOOP
# =========================
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            mark_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    main()
