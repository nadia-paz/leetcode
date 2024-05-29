class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def has_loop(self):
        """ 
        check if the linked list has a loop
        """ 
        # slow pointer
        tortoise = self.head
        # fast pointer
        hare = self.head
        temp = self.head
        
        # if the fast pointer is not None and it doesn't point to None
        while hare != None and hare.next != None:
            # move slow pointer 1 step forward
            tortoise = tortoise.next
            # move fast pointer 2 steps forward
            hare = hare.next.next

            # if pointers meet, it's a loop
            if hare == tortoise:
                return True
        return False
                
        
        


    
    
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
