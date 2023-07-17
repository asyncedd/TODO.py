import os
import platform

TODO_LISTS_DIRECTORY = "todo_lists"

MENU_ADD_TASK = "1"
MENU_REMOVE_TASK = "2"
MENU_DISPLAY_TASKS = "3"
MENU_RENAME_TODO_LIST = "4"
MENU_LOAD_TODO_LIST = "5"
MENU_EXIT = "6"


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033c", end="")


def draw_menu(todo_list_name):
    clear_screen()
    print(f"===== {todo_list_name} TODO LIST MENU =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Rename TODO List")
    print("5. Load TODO List")
    print("6. Exit")


def get_user_choice():
    return input("Enter your choice (1-6): ")


def add_task(todo_list, task):
    todo_list.add(task)
    print(f"Task added: {task}")


def remove_task(todo_list, task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task removed: {task}")
    else:
        print(f"Task not found: {task}")


def display_tasks(todo_list):
    if todo_list:
        print("Tasks:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("No tasks found.")


def rename_todo_list():
    return input("Enter the new name for the TODO list: ")


def load_tasks(todo_list_name):
    filename = os.path.join(TODO_LISTS_DIRECTORY, f"{todo_list_name}.txt")
    if not os.path.exists(filename):
        return set()

    with open(filename, "r") as file:
        return set(file.read().splitlines())


def main():
    todo_list_name = input("Enter the name for your TODO list: ")
    todo_list = load_tasks(todo_list_name)

    while True:
        draw_menu(todo_list_name)
        choice = get_user_choice()

        if choice == MENU_ADD_TASK:
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif choice == MENU_REMOVE_TASK:
            task = input("Enter task: ")
            remove_task(todo_list, task)
        elif choice == MENU_DISPLAY_TASKS:
            display_tasks(todo_list)
        elif choice == MENU_RENAME_TODO_LIST:
            todo_list_name = rename_todo_list()
        elif choice == MENU_LOAD_TODO_LIST:
            new_todo_list_name = input("Enter the name of the TODO list to load: ")
            todo_list_name = new_todo_list_name
            todo_list = load_tasks(todo_list_name)
        elif choice == MENU_EXIT:
            filename = os.path.join(TODO_LISTS_DIRECTORY, f"{todo_list_name}.txt")
            with open(filename, "w") as file:
                file.write("\n".join(todo_list))
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
