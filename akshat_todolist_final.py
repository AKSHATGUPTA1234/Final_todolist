class Todolist:
    def __init__(self):
        self.items = {}

    def create_list(self):
        list_name = input("What is the name of your list? ")
        if list_name in self.items:
            print(f"The list '{list_name}' already exists.")
        else:
            self.items[list_name] = []
            print(f"List '{list_name}' created.")
            self.view_items()  # Display all lists after creation

    def add_item(self, list_name):
        if list_name in self.items:
            while True:
                task = input("Enter the task to add (or press enter to stop): ")
                if task == "":
                    break
                self.items[list_name].append(task)
        else:
            print(f"The list '{list_name}' does not exist.")

    def remove_item(self, list_name):
        if list_name in self.items:
            while True:
                self.view_items(list_name)
                task = input("Enter the task to remove (or press enter to stop): ")
                if task == "":
                    break
                if task in self.items[list_name]:
                    self.items[list_name].remove(task)
                else:
                    print(f"Task '{task}' not found in the list '{list_name}'.")
        else:
            print(f"The list '{list_name}' does not exist.")

    def mark_as_completed(self, list_name):
        if list_name in self.items:
            while True:
                self.view_items(list_name)
                task = input("Enter the task to mark as completed (or press enter to stop): ")
                if task == "":
                    break
                if task in self.items[list_name]:
                    index = self.items[list_name].index(task)
                    completed_task = f"{task}✅"
                    self.items[list_name][index] = completed_task
                    print(f"Task '{completed_task}' marked as completed.")
                    self.items[list_name].remove(completed_task)
                else:
                    print(f"Task '{task}' not found in the list '{list_name}'.")
        else:
            print(f"The list '{list_name}' does not exist.")

    def remove_whole_list(self, list_name):
        if list_name in self.items:
            del self.items[list_name]
            print(f"List '{list_name}' removed.")
        else:
            print(f"The list '{list_name}' does not exist.")

    def view_items(self, list_name=None):
        if not self.items:
            print("No lists available.")
        elif list_name:
            if list_name in self.items:
                print(f"Tasks in list '{list_name}':")
                for task in self.items[list_name]:
                    print(f" - {task}")
            else:
                print(f"The list '{list_name}' does not exist.")
        else:
            for list_name, tasks in self.items.items():
                print(f"\nList '{list_name}':")
                for task in tasks:
                    print(f" - {task}")

    def view_all_lists(self):
        if not self.items:
            print("No lists available.")
        else:
            print("Existing lists:")
            for list_name in self.items.keys():
                print(f" - {list_name}")

    def use_task(self, list_name):
        if list_name in self.items:
            while True:
                print(f"\nUsing the todo list: {list_name}")
                print("Choose one:\n 1: Add a task\n 2: Remove a task\n 3: Mark a task as completed\n 4: View all tasks\n 5: Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    self.add_item(list_name)

                elif choice == "2":
                    self.remove_item(list_name)

                elif choice == "3":
                    self.mark_as_completed(list_name)

                elif choice == "4":
                    self.view_items(list_name)

                elif choice == "5":
                    break

                else:
                    print("Invalid choice, please try again.")
        else:
            print(f"The list '{list_name}' does not exist.")

class Starting:
    def __init__(self):
        self.todo_list = Todolist()
        self.main_menu()

    def main_menu(self):
        while True:
            print("\nTODO LIST")
            print("Choose one:\n 1: Create a todo list\n 2: Use a todo list\n 3: Remove a list\n 4: View all lists\n 5: Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.todo_list.create_list()

            elif choice == "2":
                self.todo_list.view_all_lists()  # Display all lists before asking for list name
                list_name = input("Enter the name of the list to use: ")
                if list_name in self.todo_list.items:
                    self.todo_list.use_task(list_name)
                else:
                    print(f"The list '{list_name}' does not exist.")

            elif choice == "3":
                self.todo_list.view_all_lists()
                list_name = input("Enter the name of the list to remove: ")
                if list_name in self.todo_list.items:
                    self.todo_list.remove_whole_list(list_name)
                
                    
                else:
                    print(f"The list '{list_name}' does not exist.")

            elif choice == "4":
                self.todo_list.view_all_lists()

            elif choice == "5":
                break

            else:
                print("Invalid choice, please try again.")

Starting()