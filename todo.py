todos = []


def show_menu():
    print("\n1. Add To-Do")
    print("2. View To-Dos")
    print("3. Delete To-Do")
    print("4. Exit")


def add_todo():
    task = input("Enter the task: ")
    todos.append(task)
    print(f"'{task}' added to your To-Do list.")


def view_todos():
    if not todos:
        print("Your To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todos, start=1):
            print(f"{i}. {task}")


def delete_todo():
    view_todos()
    if todos:
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print(f"'{removed}' has been removed.")
        else:
            print("Invalid number!")


while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_todo()
    elif choice == "2":
        view_todos()
    elif choice == "3":
        delete_todo()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
