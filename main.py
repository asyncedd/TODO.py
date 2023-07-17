import os
import platform

TODO_LIST_FILENAME = "todo.txt"


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


def add_task(todo_list):
    clear_screen()
    task = input("Enter task: ")
    todo_list.append(task)
    print(f"Task added: {task}")


def remove_task(todo_list):
    clear_screen()
    task = input("Enter task: ")
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task removed: {task}")
    else:
        print(f"Task not found: {task}")


def display_tasks(todo_list):
    clear_screen()
    if todo_list:
        print("Tasks:")
        for task in todo_list:
            print(f"- {task}")
    else:
        print("No tasks found.")


def rename_todo_list():
    clear_screen()
    return input("Enter the new name for the TODO list: ")


def save_tasks(todo_list):
    with open(TODO_LIST_FILENAME, "w") as file:
        file.write("\n".join(todo_list))


def load_tasks():
    if not os.path.exists(TODO_LIST_FILENAME):
        return []

    with open(TODO_LIST_FILENAME, "r") as file:
        return file.read().splitlines()


def main():
    todo_list_name = input("Enter the name for your TODO list: ")
    todo_list = load_tasks()

    menu_choices = {
        "1": add_task,
        "2": remove_task,
        "3": display_tasks,
        "4": rename_todo_list,
    }

    while True:
        draw_menu(todo_list_name)
        choice = get_user_choice()

        if choice in menu_choices:
            menu_choices[choice](todo_list)
        elif choice == "5":
            lambda _: save_tasks(todo_list)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
