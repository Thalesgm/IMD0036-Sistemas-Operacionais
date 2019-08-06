#IMD0036- Sistemas Operacionais
#Atidade 1 Criação e Finalização de Processos
#Discente:Thales Moreira
#Mat: 2014026290
import os
import array

def child():
	#print('\nA new child %d' % os.getpid())
	os._exit(0) 
	
#Function to insert ids on the array
def insert_ids(a, count):
	a.append(os.getpid())
	i = 1;
	while i <= count:
		a.append(os.fork())
		if a[i] == 0:
			child()
		i += 1
#Prints the current status of the processes
def print_status(a):
	print("Current Process Status")    
	print("Parent Process:")
	print(a[0])
	print("Children:")
	i = 1
	while i < len(a):
		print(a[i])
		i += 1
#Function to Validate the imput and kill a child process
def kill_cp(a, id):
	if id == a[0]:
		print("ID corresponds to PARENT ID. To kill parent ID, use the Kill Parent(P) Option.") 
	else:
		i = 1
		while i < len(a):
			if id == a[i]:
				os.kill(id, 15)
				print("Finishing the process")
				os.waitpid(id, 0)
				a.pop(i)
				return
			i += 1
	if i == len(a):
		print("Invalid Process ID")

def program():
	pids = array.array('i')  
	insert_ids(pids, 4)
	while True:
		print_status(pids)
		reply = input("How would you like to proceed:\nK-Kill a Process\nQ-Quit\n")
		if reply == 'K' or reply == 'k':
			option = input("C-Kill a Child Process?\nP-Kill Parent?(Suicide)\n")
			if option == 'P'or option == 'p':
				confirm = input("Are you sure you want to Kill Parent Process(Y,N)\n")
				if confirm == 'Y' or confirm == 'y':
					os.kill(os.getpid(), 9)
				else:
					continue
			elif option == 'C' or option == 'c':
				pid = int(input("Which process you want to kill?\n"))
				kill_cp(pids, pid)
		else:
			break

program()
