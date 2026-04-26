import json
menu = [
    "1. View your tasks",
    "2. Add a task",
    "3.Change a tasks status",
    "4. Delete a task",
    "5. Exit"
]
def save_tasks(tasks):
     with open("tasks.json", "w") as f:
            json.dump(tasks, f)
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def show(tasks):
     for i in range(len(tasks)):
        task = tasks[i]
        if task["done"] == False:
            status = "not done"
        else:
            status = "done"
        print(f"{i + 1}. {task['name']} - {status}")
while True:
    print("What we doing?")
    for i in menu:
        print(i)
    choic = input()
    if choic == "1":
            tasks = load_tasks()
            show(tasks)
    elif choic ==  "2":
        new_task = input("Write a task u wanna add")
        task = {
            "name": new_task,
            "done": False
        }
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    elif choic == "3":
         tasks = load_tasks()
         show(tasks)
         a = int(input("Which tasks status u wanna change?"))
         if 0 < a < len(tasks) + 1:
            st = input("Write status (true/false): ").lower() == "true"
            tasks[a - 1]["done"] = st
            save_tasks(tasks)
         else:
              print("Invalid choice")
    elif choic == "4":
         tasks = load_tasks()
         show(tasks)
         num = int(input("Which task to delete?"))
         if 0 < num <= len(tasks):
              tasks.pop(num - 1)
              save_tasks(tasks)
         else:
              print("Invalid choice")
    elif choic == "5":
         break
