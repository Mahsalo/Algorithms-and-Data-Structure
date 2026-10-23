# Detect a cycle in a singly linked list using only O(1) space (Hashmap uses O(n) space) and O(n) time
# Use Floy's Tortoise and Hare: fast pointer would always reach the slow pointer in the SLL loop


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycleSLL(head):
    slow = head
    fast = head

    while fast !=None and fast.next !=None: #continue until you hit the end or the double step reaches the end, and is short circuit eval. checking left to right
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

if __name__ == "__main__":
    # how to define a linked list
    # First make nodes then connect them

    n1 = Node(3)
    n2 = Node(2)
    n3 = Node(0)
    n4 = Node(-4)

    # Now link them
    n1.next = n2
    n2.next = n3
    n3.next = n4
    # Create the loop
    n4.next = n2

    print(hasCycleSLL(n1))
