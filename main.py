import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def draw_menu(todo_list_name):
    clear_screen()
    print(f"===== {todo_list_name} TODO LIST MENU =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Rename TODO List")
    print("5. Exit")


def get_user_choice():
    options = ["1", "2", "3", "4", "5"]
    choice = input("Enter your choice (1-5): ")

    while choice not in options:
        matching_options = [option for option in options if option.startswith(choice)]

        if matching_options:
            print("Matching options:")
            print("\n".join(matching_options))

        choice = input("Enter your choice (1-5): ")

    return choice


def add_task(todo_list):
    clear_screen()
    task = input("Enter task: ")
    todo_list.append(task)
    print(f"Task added: {task}")
    input("Press Enter to continue...")


def remove_task(todo_list):
    clear_screen()
    task = input("Enter task: ")
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task removed: {task}")
    else:
        print(f"Task not found: {task}")
    input("Press Enter to continue...")


def display_tasks(todo_list):
    clear_screen()
    if todo_list:
        print("Tasks:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("No tasks found.")
    input("Press Enter to continue...")


def rename_todo_list():
    clear_screen()
    new_name = input("Enter the new name for the TODO list: ")
    return new_name


def save_tasks(todo_list, filename):
    with open(filename, "w") as file:
        file.write("\n".join(todo_list))


def load_tasks(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return file.read().splitlines()


def main():
    todo_list_name = input("Enter the name for your TODO list: ")
    todo_list = load_tasks("todo.txt")

    while True:
        draw_menu(todo_list_name)
        choice = get_user_choice()

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            display_tasks(todo_list)
        elif choice == "4":
            todo_list_name = rename_todo_list()
        elif choice == "5":
            save_tasks(todo_list, "todo.txt")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
