class Deque():
	"""This class will define several functions which will work for deque"""

	def __init__(self):
		#Defining a list which will act as deque container
		self.mydeque = []

	def is_empty(self):
		#This method will check whether the deque is empty or not
		if len(self.mydeque) > 0:
			return False
		else:
			return True

	def add_front(self, item):
		#This method will add an item at the front of defined deque
		return self.mydeque.append(item)

	def add_rear(self, item):
		#This method will add an item at the rear of defined deque
		return self.mydeque.insert(0, item)

	def remove_front(self):
		#This method will pop an item from defined deque
		return self.mydeque.pop(0)

	def remove_rear(self):
		#This method will pop an item from defined deque
		return self.mydeque.pop()

def main():
	#Defining the main function for the deque
	d = Deque()
	#d is an object of Deque class
	while 1:
		print("1. Add at front \n2. Add at rear \n3. Remove from front \n4. Remove from rear \n5. Show \n6. Quit")
		print("\nWhat do you wanna do now?")
		case = int(input())
		#Starting something, equivalent to Switch statement in C/C++
		if case == 1:
			#In this case, we will call our add_front function
			print("Input item, you wanna add at front :")
			item = int(input())
			d.add_front(item)
			print("Congrats!",item,"has been added at front.")
		elif case == 2:
			#In this case, we will call our add_rear function
			print("Input item, you wanna add at rear :")
			item = int(input())
			d.add_rear(item)
			print("Congrats!",item,"has been added at rear.")
		elif case == 3:
			#In this case, we will call our remove_front function
			if d.is_empty() == True:
				print("Sorry, the deque is empty.")
			else:
				print(d.remove_front())
		elif case == 4:
			#In this case, we will call our remove_rear function
			if d.is_empty() == True:
				print("Sorry, the deque is empty.")
			else:
				print(d.remove_rear())
		elif case == 5:
			#In this case, we will print the current condition of our deque
			if d.is_empty() == True:
				print("Sorry, the deque is empty.")
			else:
				print("The current condition of our deque:",d.mydeque)
		elif case == 6:
			#In this case, we will quit our script
			print("The script is gonna quit.")
			quit()
		else:
			print("Oops! Wrong Choice.")
			main()
		#Finishing something, equivalent to Switch statement in C/C++

if __name__ == "__main__":
	main()