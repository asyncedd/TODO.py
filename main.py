import os
import platform

TODO_LISTS_DIRECTORY = "todo_lists"

MENU_ADD_TASK = "1"
MENU_REMOVE_TASK = "2"
MENU_DISPLAY_TASKS = "3"
MENU_RENAME_TODO_LIST = "4"
MENU_EXIT = "5"


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
    print("5. Exit")


def get_user_choice():
    return input("Enter your choice (1-5): ")


def add_task(todo_lists, todo_list_name):
    task = input("Enter task: ")
    todo_list = todo_lists.get(todo_list_name, set())
    todo_list.add(task)
    todo_lists[todo_list_name] = todo_list
    print(f"Task added: {task}")


def remove_task(todo_lists, todo_list_name):
    task = input("Enter task: ")
    todo_list = todo_lists.get(todo_list_name, set())
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task removed: {task}")
    else:
        print(f"Task not found: {task}")
    todo_lists[todo_list_name] = todo_list


def display_tasks(todo_lists, todo_list_name):
    todo_list = todo_lists.get(todo_list_name, set())
    if todo_list:
        print("Tasks:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("No tasks found.")


def rename_todo_list():
    return input("Enter the new name for the TODO list: ")


def save_tasks(todo_lists, todo_list_name):
    if not os.path.exists(TODO_LISTS_DIRECTORY):
        os.makedirs(TODO_LISTS_DIRECTORY)

    todo_list = todo_lists.get(todo_list_name, set())
    filename = os.path.join(TODO_LISTS_DIRECTORY, f"{todo_list_name}.txt")
    with open(filename, "w") as file:
        file.write("\n".join(todo_list))


def load_tasks(todo_list_name):
    filename = os.path.join(TODO_LISTS_DIRECTORY, f"{todo_list_name}.txt")
    if not os.path.exists(filename):
        return set()

    with open(filename, "r") as file:
        return set(file.read().splitlines())


def main():
    todo_lists = {}
    todo_list_name = input("Enter the name for your TODO list: ")
    todo_lists[todo_list_name] = load_tasks(todo_list_name)

    while True:
        draw_menu(todo_list_name)
        choice = get_user_choice()

        if choice == MENU_ADD_TASK:
            add_task(todo_lists, todo_list_name)
        elif choice == MENU_REMOVE_TASK:
            remove_task(todo_lists, todo_list_name)
        elif choice == MENU_DISPLAY_TASKS:
            display_tasks(todo_lists, todo_list_name)
        elif choice == MENU_RENAME_TODO_LIST:
            new_name = rename_todo_list()
            todo_lists[new_name] = todo_lists.pop(todo_list_name, set())
            todo_list_name = new_name
        elif choice == MENU_EXIT:
            save_tasks(todo_lists, todo_list_name)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
