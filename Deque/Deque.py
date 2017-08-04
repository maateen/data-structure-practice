class Deque():
    """
    @description: This class defines several methods for deque.
    """

    def __init__(self):
        # defining a list which will act as deque container
        self.mydeque = []

    def size(self):
        # returns the size of deque
        return len(self.mydeque)

    def is_empty(self):
        # checks whether the deque is empty or not
        if self.size() > 0:
            return False
        else:
            return True

    def add_front(self, item):
        # adds an item at the rear of defined deque
        return self.mydeque.insert(0, item)

    def add_rear(self, item):
        # adds an item at the front of defined deque
        return self.mydeque.append(item)

    def remove_front(self):
        # pop an item from defined deque
        if self.is_empty():
            raise ValueError("Sorry, the deque is empty.")
        else:
            return self.mydeque.pop(0)

    def remove_rear(self):
        # pop an item from defined deque
        if self.is_empty():
            raise ValueError("Sorry, the deque is empty.")
        else:
            return self.mydeque.pop()


def main():
    # defining the main function for the deque
    d = Deque()
    # d is an object of Deque class
    while 1:
        print("1. Add at front \n2. Add at rear \n3. Remove from front \n4. Remove from rear \n5. Show \n6. Quit")
        print("\nWhat do you wanna do now?")
        case = int(input())
        # Starting something, equivalent to Switch statement in C/C++
        if case == 1:
            # in this case, we will call our add_front function
            print("Input item, you wanna add at front :")
            item = input()
            d.add_front(item)
            print("Congrats!", item, "has been added at front.")
        elif case == 2:
            # in this case, we will call our add_rear function
            print("Input item, you wanna add at rear :")
            item = input()
            d.add_rear(item)
            print("Congrats!", item, "has been added at rear.")
        elif case == 3:
            # in this case, we will call our remove_front function
            if d.is_empty() == True:
                print("Sorry, the deque is empty.")
            else:
                print(d.remove_front())
        elif case == 4:
            # in this case, we will call our remove_rear function
            if d.is_empty() == True:
                print("Sorry, the deque is empty.")
            else:
                print(d.remove_rear())
        elif case == 5:
            # in this case, we will print the current condition of our deque
            if d.is_empty() == True:
                print("Sorry, the deque is empty.")
            else:
                print("The current condition of our deque:", d.mydeque)
        elif case == 6:
            # in this case, we will quit our script
            print("The script is gonna quit.")
            quit()
        else:
            print("Oops! Wrong Choice.")
            main()

if __name__ == "__main__":
    main()
