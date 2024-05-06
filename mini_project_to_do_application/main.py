def main_menu():
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    title = input("Enter the title of the task: ")
    tasks.append({'title': title, 'status': 'Incomplete'})
    print("Task added.")

def view_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} - {task['status']}")
    else:
        print("No tasks to display.")

def mark_task_complete(tasks):
    if tasks:
        index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['status'] = 'Complete'
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks available.")

def delete_task(tasks):
    if tasks:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

def main():
    tasks = []
    while True:
        main_menu()
        choice = input("Select an option: ")
        try:
            choice = int(choice)
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Thank you for using the To-Do List App. Goodbye!")
                break
            else:
                print("Please select a valid option (1-5).")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
