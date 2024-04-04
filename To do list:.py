class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
        print("Task added successfully!")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "✓" if task.completed else " "
                print(f"{index}. [{status}] {task.description}")

    def update_task(self, task_number, new_description):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].description = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            task_number = int(input("Enter task number to update: "))
            new_description = input("Enter new task description: ")
            todo_list.update_task(task_number, new_description)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
