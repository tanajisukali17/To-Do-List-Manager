tasks = []

while True:
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        task = input("Enter the new task: ")
        tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    elif choice == '2':
        if not tasks:
            print("Your to-do list is empty")
        else:
            print("\nTo-Do List")
            for idx, task in enumerate(tasks, 1):
                status = "Completed" \
                    if task['completed'] else "Pending"
                print(f"{idx}. {task['task']} [{status}]")

    elif choice == '3':
        if not tasks:
            print("Your to-do list is empty")
        else:
            print("\nTo-Do List")
            for idx, task in enumerate(tasks, 1):
                status = "Completed" \
                    if task['completed'] else "Pending"
                print(f"{idx}. {task['task']} [{status}]")

            task_num = int(input("Enter the task number to mark as completed : "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == '4':
        if not tasks:
            print("Your to-do list is empty")
        else:
            print("\nTo-Do List")
            for idx, task in enumerate(tasks, 1):
                status = "Completed" \
                    if task['completed'] else "Pending"
                print(f"{idx}. {task['task']} [{status}]")

            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"Task '{deleted_task['task']}' deleted.")
            else:
                print("Invalid task number.")

    elif choice == '5':
        print("Exit")
        break

    else:
        print("Invalid choice. Please select a valid option.")