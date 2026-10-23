## Find the starting point of a cycle in a singly LL
## Use Floyd's Tortoise and Hare algo. but remember after detecting the cycle, you must continue to find the starting point
## After finding the cycle, keep one pointer (now p1) at th ecollision and the reset another one at the beginning (say p2)
## both move 1 step at the time (same direction as before)
from email.quoprimime import header_check


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def StartOfCycle(head):
    slow = head
    fast = head
    has_cycle = False

    # Phase one: detect the cycle
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("Cycle detected! Now finding the start point of the cycle")
            has_cycle = True
            break

    # End if no cycle
    if not has_cycle:
        return None

    # Phase tw: find the starting point
    slow = head
    while slow !=fast: # they must defo. reach each other
        slow = slow.next
        fast = fast.next

    return slow



if __name__=="__main__":
    # First make the nodes
    n1 = Node(3)
    n2 = Node(2)
    n3 = Node(0)
    n4 = Node(-4)

    # Then link them
    n1.next = n2
    n2.next = n3
    n3.next = n4

    # now make the loop
    n4.next = n2

    print(StartOfCycle(n1).val) # show the value, return the node
