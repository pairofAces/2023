# Remove Duplicates From Linked List

# You're given the head of singly linked list, where the nodes are in sorted order.
# Create a function that returns a modified version of the Linked List that doesn't
# contain any nodes with duplicate values. 

# The Linked List should be modified in place, meaning there shouldn't be a new
# list being produced. 
    # the modified list should still be in sorted order.

# Each LinkedList node has an integer (value) and a (next) node pointing to
# the next node in the list or to None/null, if it's the tail of the list. 

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return linkedList

# test
linked_list = LinkedList(1)
linked_list.next = LinkedList(2)
linked_list.next.next = LinkedList(2)
linked_list.next.next.next = LinkedList(3)
linked_list.next.next.next.next = LinkedList(3)
linked_list.next.next.next.next.next = LinkedList(3)

result = removeDuplicatesFromLinkedList(linked_list)

while result is not None:
    print(result.value)
    result = result.next