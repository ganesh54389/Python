class ToDoList:
    def __init__(self):
        self.tasks=[ ]# tasks are added to empty list
    def add_task(self,task):
        self.tasks.append({"task":task,"completed":False})
        print("Task added succsesfully")
    def remove_task(self,task):
        for i in self.tasks:
            if i["task"]==task :
                self.tasks.remove(i)
                print("task removed succsesfully")
                return
        print("task not found in the list")

    def mark_completed(self,task):
        for t in self.tasks:
            if t["task"]==task:
                t["completed"]=True
                print("task marked as completed")
                return
        print("task not found in the list")

    def display_task(self):
        if self.tasks:
            print("tasks")
            for i,t in enumerate(self.tasks,start=1):
                status="completed" if t["completed"] else "not completed"
                print(f"{i}.{t["task"]}-{status}")
        else:
            print("no task in the list ")


   
    
object=ToDoList()
while True:
        print("to do list menu")
        print("1.Add a Task")
        print("2.Remove a task")
        print("3.Mark a taask as completed ")
        print("4.Display task")
        print("5.Exit")      
        choice=input("enter your choice(1 to 5):")
        if choice=="1":
            task=input("enter your task:")
            object.add_task(task)
        elif choice=="2":
            task=input("enter your task:")
            object.remove_task(task)
        elif choice=="3":
            task=input("enter task to mark as completed ")
            object.mark_completed(task)
        elif choice=="4":
            object.display_task()
        elif choice=="5":
            print("exiting")
            break
        else:
            print("invalid choice")       

                    

          








