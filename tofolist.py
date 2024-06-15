def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"'{task}' added to the list.")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"'{task}' removed from the list.")
    else:
        print(f"'{task}' not found in the list.")

def view_tasks(tasks):
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()