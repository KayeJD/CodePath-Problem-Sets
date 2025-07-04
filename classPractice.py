# 1. 
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        # list of mutual friends
        mutuals_list = []

        # convert to sets and find the overlap 
        mutuals_set = set(self.friends).intersection(set(new_contact.friends))
        
        # convert intersection set back to list, print list 
        for mutual in list(mutuals_set):
            mutuals_list.append(mutual.name)
        
        return mutuals_list
        
# TEST
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))


# 2. 
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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

# print_linked_list(kk_slider)


# 3. 
def add_first(head, task):
    # create new node called task
    new_task = Node("check turnip prices")
    # make the next the original head
    new_task.next = head
    head = new_task
    return head

# For testing
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))


# 4. 
def halve_list(head):
    curr = head

    while curr:
        curr.value = curr.value / 2
        curr = curr.next

    return head 

# For Testing 
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))


# 5. 

def delete_tail(head):
    curr = head
    # do while loop until there is no curr.next.next
    # when curr.next is None, remove curr and set curr.next = None

    while curr.next.next:
        curr = curr.next
    curr.next = None

    return head

# For Testing 
butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))


#6
def find_min(head):
    min = head.value

    # iterate through list
    curr = head 
    # break when curr is none
    while curr.next:
        # comapare curr.value with min and update min
        if curr.next.value < min:
            min = curr.next.value
        curr = curr.next 
    # return min value
    return min

    
# For testing 
head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))


# 7. 
def delete_item(head, item):
    # iterate through linked list
    curr = head
     
    # edge case z wy not
    if curr.value == item:
        head = curr.next 
        curr.next = None
        return head
    
    while curr.next: # type: ignore
        if curr.next.value == item: # type: ignore
            if curr.next.next is None: # type: ignore
                # if curr.next.next is none, then just set curr.next = none
                curr.next = None
            else:
                # if curr.value = item, then curr.next = curr.next.next
                curr.next = curr.next.next # type: ignore
        curr = curr.next # type: ignore
            
    # return head
    return head

# For testing 
slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))

