tasks = ["eat","sleep","code"]
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}") 
new_task = input("type new task")
tasks.append(new_task)
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}") 

