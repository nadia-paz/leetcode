class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):

        # if ll is empty
        if self.head == None:
            return self
        length = 0
        middle = 0
        # to save middle node
        middle_node = self.head
        # to count the length of the ll
        temp = self.head
        
        while temp.next != None:
            length += 1
            # calculate the ceiling devision if the length is even
            new_middle = - (length // -2) # ceiling devision
            # move the middle
            if new_middle != middle:
                middle = new_middle
                middle_node = middle_node.next
            temp = temp.next
        return middle_node



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""