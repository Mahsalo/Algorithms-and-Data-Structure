## Find the  middle point of the linked list (somehow we should be sure it does not include a cycle)
## If even number of elements, it returns the second, if odd, exactly the middle

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def middleNode(head):
    slow = head
    fast = head

    while fast !=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next

    return slow

if __name__ == "__main__":

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = None 

    print(middleNode(n1).val)
