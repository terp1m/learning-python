new_task = input("Write a new task")
tasks.append({"name": new_task, "done": False})
show(tasks)


tasks = [
    {"name": "eat", "done": False},
    {"name": "sleep", "done": False}
]

if num < 1 or num > len(tasks):
    print("Invalid choice")
else:
    p = input("Write status (true/false): ").lower() == "true"
    tasks[num - 1]["done"] = p
