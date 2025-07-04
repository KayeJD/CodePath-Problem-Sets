# Advanced Problem Set Version 1

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Q1 ================================================================================================
''' Greatest Node
Write a function find_max() that takes in the head of a linked list and returns the maximum value in the linked list. You can assume the linked list will contain only numeric values.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def find_max(head):
    max = 0
    curr = head
    while curr:
        if curr.value >= max:
            max = curr.value

        curr = curr.next

    return max

# TEST
head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))

# Q2 ================================================================================================
''' Remove Tail
The following code incorrectly implements the function remove_tail(). When correctly implemented, remove_tail() accepts the head of a singly linked list and removes the last node (the tail) in the list. The function should return the head of the modified list.

Step 1: Copy this code into Replit.

Step 2: Create your own test cases to run the code against. Use print statements, print_linked_list(), and the stack trace to identify and fix any bugs so that the function correctly removes the last node from the list.
'''

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return head 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

# TEST
head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

# Q3 ================================================================================================
''' Delete Duplicates in a Linked List
Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). The resulting list should maintain sorted order. Return the head of the linked list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def delete_dupes(head):
    # create prev variable that keeps track of the previous node
    # utilize curr variable to step through the linked list

    prev = head # start prev at the head
    curr = head.next # start iterating at the second value

    while curr:
        if curr.value == prev.value: #checking if duplicate from previous
            prev.next = curr.next # skip the current element (deleting it), by making the prev.next

        curr = curr.next
        prev = prev.next

    return head

# TEST
head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

# Q4 ================================================================================================
''' Does it Cycle?
A variation of the two-pointer technique introduced earlier in the course is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to write a function has_cycle() that returns True if the list has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def has_cycle(head):
    if not head:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

# TEST
peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next # type: ignore

print(has_cycle(peach))

# Q5 ================================================================================================
''' Remove nth Node From End of List
Given the head of a linked list and an integer n, write a function remove_nth_from_end() that removes the nth node from the end of the list. The function should return the head of the modified list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def remove_nth_from_end(head, n):
    prev = head
    curr = head.next

    # Reach the n-1th element
    while n > 1:
        if curr and curr.next:
            prev = prev.next
            curr = curr.next
        n -= 1

    prev.next = curr.next

    return head

# TEST
head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))

# Standard Problem Set Version 2