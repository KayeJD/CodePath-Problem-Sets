from collections import deque 

class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def merge_orders(order1, order2):
    # make order1 the merged 
    # if empty node in one, just replace with the other tree
    
    # do in order traversal just to hit all 
        # else
            # order1curr.val += order2.vall

    if not order1 and not order2:
        return None
    elif not order1 and order2:
        return order2
    elif order1 and not order2:
        return order1
    else: 
        new_node = TreeNode(order1.val + order2.val)
        new_node.left = merge_orders(order1.left, order2.left)
        new_node.right = merge_orders(order1.right, order2.right)
        return new_node 
    # elif order1 and order2:
    #     return order1 + order2
    
    # merge_orders(order1, order2)

    # merge_orders(order1, order2)



# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))









class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):

    if design is None: 
        return []
    
    res = []
    queue = deque()
    queue.append(design)

    while queue:
        visited = []
        for i in range(len(queue)):
            node = queue.popleft()
            if node is not None: 
                visited.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                
        
        if visited: 
            res.extend(visited)
    return res


croquembouche = Puff("Vanilla", Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), Puff("Strawberry"))
print(print_design(croquembouche))


def max_tiers(cake):
    if not cake: 
        return 0 
    
    queue = deque()
    queue.append(cake)
    count = 0
    
    while queue:
        count += 1

        # this is basically through the height
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
                
    return count
    
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))





def max_tiers2(cake):
    if not cake: 
        return 0 
    
    queue = deque()
    queue.append(cake)
    count = 0


    
    while queue:
        count += 1

        # this is basically through the height
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
    return count


cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers2(cake))

def can_fulfill_order(inventory, order_size):
    pass