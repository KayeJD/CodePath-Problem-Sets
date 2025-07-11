class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
	# Temp head
    # print(suspect_ratings)
    partition = suspect_ratings
    # print(partition)
    part_end = suspect_ratings

    current = suspect_ratings.next

    while current:
        if current.value > threshold:
            # make a new node tmpNOde
            tmpNode = Node(current.value)
            tmpNode.next = partition
            # need to move partition pointer
            partition = tmpNode
        elif current.value <= threshold:
            # add it tot eh end of your partition ll
            tmpNode = Node(current.value)
            part_end.next = tmpNode
            part_end = tmpNode

        current = current.next
    
    return partition

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print(suspect_ratings.value)

print_linked_list(partition(suspect_ratings, 3))