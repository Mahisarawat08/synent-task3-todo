tasks = []

while True:
    print("\n" + "=" * 40)
    print("         TO-DO LIST MENU")
    print("=" * 40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter new task: ").strip()
        if task:
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"'{removed}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")