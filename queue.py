class Queue():
	"""This class will define several functions which will work for queue"""

	def __init__(self):
		#Defining a list which will act as queue container
		self.myqueue = []

	def is_empty(self):
		#This will check whether the queue is empty or not
		if len(self.myqueue) > 0:
			return False
		else:
			return True

	def enqueue(self, item):
		#This will enqueue a item to the defined queue
		return self.myqueue.insert(0, item)
		#innsert(0, item) will insert "item" to the 0th position of the defined list

	def dequeue(self):
		#This will dequeue an item from defined queue
		return self.myqueue.pop()

def main():
	#Defining the main function for the queue
	q = Queue()
	while 1:
		print("1. Enqueue \n2. Dequeue \n3. Show \n4. Quit")
		print("\nWhat do you wanna do now?")
		case = int(input())
		#Starting something, equivalent to Switch statement in C/C++
		if case == 1:
			#In this case, we call our enqueue function
			print("Input item, you wanna enqueue:")
			item = int(input())
			q.enqueue(item)
			print("Congrats!",item,"has been enqueued.")
		elif case == 2:
			#In this case, we call our dequeue function
			if q.is_empty() == True:
				print("Sorry, the queue is empty.")
			else:
				print(q.dequeue(),"has been dequeued.")
		elif case == 3:
			#In this case, we will print the current condition of our queue
			if q.is_empty() == True:
				print("Sorry, the queue is empty.")
			else:
				print("The current condition of our queue:",q.myqueue)
		elif case == 4:
			print("The script is gonna quit.")
			quit()
		else:
			print("Oops! Wrong Choice.")
			main()
		#Finishing something, equivalent to Switch statement in C/C++

if __name__ == "__main__":
	main()