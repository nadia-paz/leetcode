class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        """
        Swaps the nodes (not values!) of each pair of nodes in double linked list
        1 <-> 2 <-> 3 <-> 4 turns into 2 <-> 1 <-> 4 <-> 3
        1 <-> 2 <-> 3 <-> 4 <-> 5 turns into 2 <-> 1 <-> 4 <-> 3 <-> 5
        Print statements to track the progress and catch missed connections
        """

        # if the length of the list is 0 or 1 return without changes
        if self.length <= 1:
            return self
        
        # set the dummy variable curr to move through the DLL
        curr = self.head
        # move the head of the list to the 2nd node
        self.head = curr.next
        
        while curr is not None:
            # if the curr points to None, there is no pair, break
            if curr.next is None:
                break
            # first and second - pair of nodes to swap
            first, second = curr, curr.next
            print(f'{first.value} {second.value}')
            # move current for the next interation
            curr = second.next
            
            # if curr:
            #     print(f'Currnet value: {curr.value}')
            # print("---")
            # self.print_list()


            # connect the previous pair of nodes to the current pair
            if first.prev:
                first.prev.next = second
            
            # change pointers
            first.next = curr
            # print(f'First next points to {curr.value if curr else curr}')
            second.prev = first.prev
            # print(f'Second prev points to {first.prev.value if first.prev else first.prev}')
            first.prev = second
            # print(f'First prev points to {second.value if second else second}')
            second.next = first
            # print(f'Second next points to {first.value if first else first}')
            # print("-*-")

            # connect current node to the pair of nodes
            if curr:
                curr.prev = first
                # print(f'Current pointers:\n\
                #     <- {curr.prev.value if curr.prev else curr.prev}\n\
                #     -> {curr.next.value if curr.next else curr.next}')
            
            # if the number was odd, tail doesn't change, else, move tail to the new node
            if self.length %2 == 0:
                self.tail = first
        

            


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""