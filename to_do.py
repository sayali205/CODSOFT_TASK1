task=[]
def show():
	print("To DO List\n")
	print("1.View Task")
	print("2.Add Task")
	print("3.Update Task")
	print("4.Delete Task")
	print("5.Exit Task")
def view():
	if not task:
		print("No task List")
	else:
		print("\nYour Task:")
		for index,task in enumerate(task,start=1):
			print(f"{index}.{task}")
def add():
	task=input("Enter your task:")
	task.append(task)
	print("Task added Successfully.")
def update():
        view()
        if task:
                 try:
                         taskn=int(input("Enter task no to update:"))
                         if 1<=taskn<=len(task):
                                 ntask=input("Enter new Task:")
                                 task[taskn]=ntask
                                 print("=Task Successfully updated..")
                         else:
                                print("Invalid Task number..")
                 except ValueError:
                        print("Please Enter valid Number..")
def delete():
	view()
	if task:
		try:
			taskn=int(input("Enter task number to dalate:"))
			if 1<=taskn<=len(task):
				task.pop(taskn-1)
				print("Task is Successfully Deleted..")
			else:
				print("Invalid Task number...")
		except ValueError:
			print("Please enter valid Number..")
while True:
	show()
	c=input("Enter your Choice :")
	if c=='1':
		view()
	elif c=='2':
		add()
	elif c=='3':
		update()
	elif c=='4':
		delete()
	elif c=='5':
		print("Exiting to do list .")
		break
	else:
		print("Invalid choice.Please enter number between 1 to 5.")
		
