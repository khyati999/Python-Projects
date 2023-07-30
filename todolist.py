class Task:
    def __init__(self, name):
        self.name = name
        self.is_completed=False

    def __str__(self):
        status = "Done" if self.is_completed else "Not Done"
        return f"{self.name} - {status}"
class TodoList:
        def __init__(self):
            self.tasks = []     #List of task

        def add_task(self,task_name):
            task = Task(task_name)
            self.tasks.append(task)

        def view_task(self):
            if not self.tasks:
                print("No task found!!")
            else:
                for index, task in enumerate(self.tasks,1):
                    print(f"{index}. {task}")
    
        def mark_completed(self, task_index):
            if 1<=task_index <=len(self.tasks):
                self.tasks[task_index - 1].is_completed =True

            else:
                print("Invalid Task Index.")
        def remove_completed_tasks(self):
            self.tasks = [task for task in self.tasks if not task.is_completed]

def main():
    todo_list= TodoList()
    while True:
        print("\n----To Do List -----")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task")
        print("4. Remove Task")
        print("5. Close")

        choice= input("Enter your choice from 1-5: ")
        if choice == '1':
            task_name=input("Enter Task Name: ")
            todo_list.add_task(task_name)

        elif choice == '2':
            todo_list.view_task()

        elif choice == '3':
            task_index= int(input("Enter the task number: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            todo_list.remove_completed_tasks()
        elif choice == '5':
            print("Thanks for using the the todo list system \n")
            break
        else:
            print("Invalid task")
    
if __name__ =="__main__":
    main()