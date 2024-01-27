# To do List Program
# Joao Pedro Costa
# This is a program where you can add what you have to do

def interface(tasks, ids):
    while True:
        print("1 - Insert task")
        print("2 - Delete task")
        print("3 - Set task concluded")
        print("4 - Show all tasks")
        print("5 - Exit")
        option = input("Insert your choice: ")
        if option == "1":
            insert_task(tasks, ids)
        elif option == "2":
            delete_task(tasks, ids)
        elif option == "3":
            concluded_task(tasks, ids)
        elif option == "4":
            show_all_tasks(tasks, ids)
        elif option == "5":
            break

def insert_task(tasks, ids):
    task = input("\nInsert your task: ")
    if not ids:
        id = 1
    else:
        id = ids[-1] + 1
    tasks.append(task)
    ids.append(id)
    print("\n")

def delete_task(tasks, ids):
    task_id = int(input("\nInsert id of your task: "))
    if task_id in ids:
        index = ids.index(task_id)
        tasks.pop(index)
        ids.pop(index)
    else:
        print("Task not found.\n")

def concluded_task(tasks, ids):
    task_id = int(input("\nInsert id of the task that you conclude: "))
    if task_id in ids:
        index = ids.index(task_id)
        tasks[index] += " - Concluded"
    else:
        print("Task not found.\n")
    print("\n")

def show_all_tasks(tasks, ids):
    print("\nAll tasks:")
    for i in range(len(tasks)):
        print(f"{ids[i]} - {tasks[i]}")
    print("\n")

def main():
    tasks = []
    ids = []
    interface(tasks, ids)

main()
