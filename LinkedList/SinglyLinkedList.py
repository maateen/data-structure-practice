class Node():
    """
    @description: This class will act as node for Linked List and will hold data.
    @params:
        item: item means data item
        next_node: a pointer, indicates the address of next node
    """

    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node

    def get_item(self):
        # returns the data item
        return self.item

    def get_next_node(self):
        # returns the address of new node
        return self.next_node

    def set_next_node(self, new_node):
        # preserve the address of new node in self.next_node (class variable)
        self.next_node = new_node


class SinglyLinkedList():
    """
    @description: This class defines several methods for Singly Linked List.
    @params:
        head: indicates the first node of list
    """

    def __init__(self, head=None):
        self.head = head

    def add(self, item):
        # add an item to the head of the list
        new_node = Node(item)
        new_node.set_next_node(self.head)
        self.head = new_node

    def append(self, item):
        # adds an item to the end of the list
        current = self.head
        if current:
            while current.get_next_node():
                current = current.get_next_node()
            current.set_next_node(Node(item))
        else:
            self.head = Node(item)

    def insert(self, position, item):
        # adds an item to an exact position of the list
        if position == 0:
            self.add(item)
        elif position == self.size():
            self.append(item)
        elif position > self.size():
            print("Position index is out of range.")
        else:
            current = self.head
            index = 0
            while current:
                if index != position:
                    previous = current
                    current = current.get_next_node()
                    index += 1
                else:
                    new_node = Node(item, current)
                    previous.set_next_node(new_node)

    def is_empty(self):
        # checks whether the list is empty or not
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        # returns the total items number of the list
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def index(self, item):
        # returns the index position of an item in the list
        current = self.head
        index = 0
        while current:
            if current.get_item() == item:
                return index
            else:
                current = current.get_next_node()
                index += 1
        return None

    def search(self, item):
        # checks whether an item exist in the list or not
        current = self.head
        found = False
        while current and not found:
            if current.get_item() == item:
                found = True
            else:
                current = current.get_next_node()
        if current is None:
            raise ValueError("Item is not in the list.")
        return found

    def remove(self, item):
        # removes an item from the list
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_item() == item:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if current is None:
            raise ValueError("Item is not in the list.")
        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next_node(current.get_next_node())

    def pop(self, position=None):
        # removes the last item of the list
        current = self.head
        previous = None
        while current.get_next_node():
            previous = current
            current = current.get_next_node()
        if current == self.head:
            self.head = None
        else:
            previous.set_next_node(None)
        return current.get_item()

def main():
    # defining the main function for the singly linked list
    mylist = SinglyLinkedList()
    # mylist is an object of SinglyLinkedList class
    while True:
        print("1. Add \n2. Append \n3. Insert \n4. Get Size \n5. Search \n6. Get Index \n7. Remove \n8. Pop")
        print("\nWhat do you wanna do now?")
        case = int(input())
        # starting something, equivalent to Switch statement in C/C++
        if case == 1:
            # in this case, we will call our add method
            print("Input item, you wanna add to list:")
            item = input()
            mylist.add(item)
            print("Congrats!", item, "has been added.")
        elif case == 2:
            # in this case, we will call our add method
            print("Input item, you wanna append to list:")
            item = input()
            mylist.append(item)
            print("Congrats!", item, "has been appended.")
        elif case == 3:
            # in this case, we will call our add method
            print("Input position:")
            position = int(input())
            print("Input item, you wanna push to list:")
            item = input()
            mylist.insert(position, item)
        elif case == 4:
            # in this case, we will call our size method
            print("There are", mylist.size(), "items in the list.")
        elif case == 5:
            # in this case, we will call our search method
            print("Input item, you wanna search in list:")
            item = input()
            print(mylist.search(item))
        elif case == 6:
            # in this case, we will call our insert method
            print("Input item, you wanna know its index:")
            item = input()
            index = mylist.index(item)
            print(item, "is in index number", index)
        elif case == 7:
            # in this case, we will call our remove method
            if mylist.is_empty():
                print("Sorry, the list is empty.")
            else:
                print("Input item, you wanna remove:")
                item = input()
                mylist.remove(item)
                print("Congrats!", item, "has been removed.")
        elif case == 8:
            # in this case, we will call our pop method without position
            if mylist.is_empty():
                print("Sorry, the list is empty.")
            else:
                item = mylist.pop()
                print("Congrats!", item, "has been removed.")

if __name__ == '__main__':
    main()