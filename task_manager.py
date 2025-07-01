def add_task(tasks):
    description = input("Enter task description: ")
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "status": "To Do"})
    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for taks in tasks:
        print(f"[{task['id']}] {task['description']} - {[task['status']]}")


def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            new_status = input("New status (To Do / In progress / Done): ")
            task["status"] = new_status
            save_tasks(tasks)
            print("Task updated.")
            return
        print("Task not found.")


def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted.")


def main():
    tasks = load_tasks()
    while true:
        print("\nOptions: add / List / update / delete / quit")
        choice = input("What do you want to do? ").strip().lower()

        if choice == "add":
            add_task(tasks)
        elif choice == "list":
            list_tasks(tasks)
        elif choice == "update":
            update_task(tasks)
        elif choice == "delete":
            delete_task(tasks)
        elif choice == "quit":
            print("Goodbye")
            break
        else:
            print("Invalid option.")
