
class LinkedList:
    def __init__(self):
        self.head = None
       
    ### Traverse a linked list    
    def traverse_list(self):
        if self.head is None:
            print("List has no elements")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
    ### Inserting a value in the beggining
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node       

    ### Inserting a value to the end of the list
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node                     
            return 
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


        
l = LinkedList()
first_node = Node(5)
l.head = first_node
second_node = Node(11)
first_node.next = second_node
l.traverse_list()
l.insert_at_start(22)
l.traverse_list()
l.insert_at_end(110)
l.traverse_list()
