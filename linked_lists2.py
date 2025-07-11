# Advanced Set 1, Session 1

# Q1 ================================================================================================
''' Selective DNA Deletion
As a biologist, you are working on editing a long strand of DNA represented as a linked list of nucleotides. Each nucleotide in the sequence is represented as a node in the linked list, where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.

Given the head of the linked list dna_strand and two integers m and n, write a function edit_dna_sequence() that simulates the selective deletion of nucleotides in a DNA sequence. You will: - Start at the beginning of the DNA strand. - Retain the first m nucleotides from the current position. - Remove the next n nucleotides from the sequence. - Repeat the process until the end of the DNA strand is reached.

Return the head of the modified DNA sequence after removing the mentioned nucleotides.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

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

def edit_dna_sequence(dna_strand, m, n):
    # create pointer to iterate through the list

    # start a while loop for iteration
        # for loop (for first m elements)
            # skip the first m elements
        # for loop (for next n elements)
            # delete the nodes

    curr = dna_strand
    head = curr  # Keep track of the head of the modified list
    prev = None  # This will point to the last retained node

    while curr:
        # Retain the first m nucleotides
        for i in range(m):
            if curr is None:  # Check if curr is None before accessing
                return head  # Return the modified list if we reach the end
            prev = curr  # Update prev to the current node
            curr = curr.next  # Move to the next node

        # Delete the next n nucleotides
        for i in range(n):
            if curr is None:  # Check if curr is None before accessing
                break  # Break if we reach the end
            curr = curr.next  # Move to the next node

        # Link the last retained node to the next node after deletion
        prev.next = curr  # type: ignore # Connect the last retained node to the current node
        
    return head  # Return the head of the modified list

# Testing
dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

''' Example Output
1 -> 2 -> 6 -> 7 -> 11 -> 12
Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  
(1 -> 2) show in black nodes.
Delete the next (n = 3) nodes (3 -> 4 -> 5) show in red nodes.
Continue with the same procedure until reaching the tail of the Linked List.
'''

