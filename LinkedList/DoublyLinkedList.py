class Node():
    """
    @description: This class will act as node for Linked List and will hold data.
    @params:
        item: item means data item
        previous_node: a pointer, indicates the address of previous node
        next_node: a pointer, indicates the address of next node
    """

    def __init__(self, item=None, previous_node=None, next_node=None):
        self.item = item
        self.previous_node = previous_node
        self.next_node = next_node


class DoublyLinkedList():
    """
    @description: This class defines several methods for Doubly Linked List.
    @params:
        head: indicates the first node of list
        tail: indicates the last node of list
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def appendleft(self, item):
        # adds an item to the head of the list
        new_node = Node(item)
        new_node.previous_node = None
        new_node.next_node = self.head
        if self.head is None:
            self.tail = new_node
        else:
            self.head.previous_node = new_node
        self.head = new_node

    def append(self, item):
        # adds an item to the end of the list
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.previous_node = self.tail
            new_node.next_node = None
            self.tail.next_node = new_node
            self.tail = new_node

    def insert(self, position, item):
        # adds an item to an exact position of the list
        if position == 0:
            self.appendleft(item)
            print(item, "inserted to position", position)
        elif position == self.size():
            self.append(item)
            print(item, "inserted to position", position)
        elif position > self.size():
            print("Index out of range")
        else:
            current = self.head
            index = 0
            while current:
                if index != position:
                    previous = current
                    current = current.next_node
                    index += 1
                else:
                    new_node = Node(item, previous, current)
                    previous.next_node = new_node
                    current.previous_node = new_node
                    current = False
                    print(item, "inserted to position", position)

    def is_empty(self):
        # checks whether the list is empty or not
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        # returns the total items number of the list
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def index(self, item):
        # returns the index position of an item in the list
        current = self.head
        index = 0
        while current:
            if current.item == item:
                return index
            else:
                current = current.next_node
                index += 1
        return None

    def search(self, item):
        # checks whether an item exist in the list or not
        current = self.head
        found = False
        while current and not found:
            if current.item == item:
                found = True
            else:
                current = current.next_node
        if current is None:
            print("Item not found")
        return found

    def popleft(self):
        # removes the first item of the list
        if self.is_empty():
            print("Empty list")
        else:
            current = self.head
            next_node = current.next_node
            if next_node is None:
                temp = current.item
                del current
                self.head = self.tail = None
                return temp
            else:
                temp = current.item
                del current
                next_node.previous_node = None
                self.head = next_node
                return temp

    def pop(self):
        # removes the last item of the list
        if self.is_empty():
            print("Empty list")
        else:
            current = self.tail
            previous = current.previous_node
            if previous is None:
                temp = current.item
                del current
                self.head = self.tail = None
                return temp
            else:
                temp = current.item
                del current
                previous.next_node = None
                self.tail = previous
                return temp

    def remove(self, item):
        # removes an item from the list
        if self.is_empty():
            print("Empty list")
        else:
            current = self.head
            previous = None
            found = False
            while current and not found:
                if current.item == item:
                    found = True
                else:
                    previous = current
                    current = current.next_node
            if current is None:
                print("Item not found")
            elif previous is None:
                self.popleft()
                print(item, "removed")
            else:
                temp = current.next_node
                del current
                print(item, "removed")
                previous.next_node = temp
                temp.previous_node = previous

    def printlist(self):
        if self.is_empty():
            print("Empty list")
        else:
            current = self.head
            while current:
                print(current.item)
                current = current.next_node

def main():
    # defining the main function for the Doubly linked list
    mylist = DoublyLinkedList()
    # mylist is an object of DoublyLinkedList class
    while True:
        print("1. Append to Left \n2. Append \n3. Insert \n4. Get Size \n5. Search \n6. Get Index \n7. Remove \n8. Pop from Left \n9. Pop \n10. Print List \n11. Quit")
        print("\nWhat do you wanna do now?")
        case = int(input())
        # starting something, equivalent to Switch statement in C/C++
        if case == 1:
            # in this case, we will call our appendleft method
            print("Input item, you wanna appendleft to list:")
            item = input()
            mylist.appendleft(item)
            print("Congrats!", item, "has been added.")
        elif case == 2:
            # in this case, we will call our appendleft method
            print("Input item, you wanna append to list:")
            item = input()
            mylist.append(item)
            print("Congrats!", item, "has been appended.")
        elif case == 3:
            # in this case, we will call our appendleft method
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
                print("Empty list")
            else:
                print("Input item, you wanna remove:")
                item = input()
                mylist.remove(item)
        elif case == 8:
            # in this case, we will call our pop method without position
            if mylist.is_empty():
                print("Empty list")
            else:
                item = mylist.popleft()
                print(item, "removed")
        elif case == 9:
            # in this case, we will call our pop method without position
            if mylist.is_empty():
                print("Empty list")
            else:
                item = mylist.pop()
                print(item, "removed")
        elif case == 10:
            # in this case, we will print our list
            if mylist.is_empty():
                print("Empty list")
            else:
                mylist.printlist()
        elif case == 11:
            # in this case, we will quit our script
            print("The script is gonna quit.")
            quit()
        else:
            print("Oops! Wrong Choice.")
            main()

if __name__ == '__main__':
    main()