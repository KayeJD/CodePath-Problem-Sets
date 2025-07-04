# Standard set 1 

class Villager:
    def __init__(self, name, species, catchphrase, personality):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.personality = personality
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        if all(char.isalpha() or char.isspace() for char in new_catchphrase) and len(new_catchphrase) <= 20:
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invaliud catchphrase")

    def add_item(self, item_name):
        if item_name in ("acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"):
            self.furniture.append(item_name)

    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory empty")

        furnitureCount = {}
        
        for item in self.furniture:
            if item not in furnitureCount:
                furnitureCount[item] = 1
            else:
                furnitureCount[item] += 1
        
        output = f""

        for furniture, quant in furnitureCount.items():
            output += f"{furniture}: {quant}, "

        print(output)

# Q1 ================================================================================================
'''
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".
'''

apollo = Villager("Apollo", "Eagle", "pah", "")

# Check
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 

# Q2 ================================================================================================
'''
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

Step 2: Create a second instance of Villager in a variable named bones.

The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.
'''

bones = Villager("Bones", "Dog", "yip yip", "")

# Check
print(bones.greet_player("Tram"))

# Q3 ================================================================================================
'''
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".
'''

bones.catchphrase = "ruff it up"

# Check
print(bones.greet_player("Samia"))

# Q4 ================================================================================================
'''
In the previous exercise, we accessed and modified a player’s catchphrase attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
Otherwise, it should print out "Invalid catchphrase".
Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.
''' 

# Check
alice = Villager("Alice", "Koala", "guvnor", "")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

# Q5 ================================================================================================
'''
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".
'''

# Check
alice = Villager("Alice", "Koala", "guvnor", "")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

# Q6 ================================================================================================
'''
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
'''

# Check
alice = Villager("Alice", "Koala", "guvnor", "" )

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()

# Q7 ================================================================================================
'''
The Villager class has been updated below to include the new string attribute personality representing the character's personality type.

Outside of the Villager class, write a function of_personality_type(). Given a list of Villager instances townies and a string personality_type as parameters, return a list containing the names of all villagers in townies with personality personality_type. Return the names in any order.

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
    
def of_personality_type(townies, personality_type):
    pass
'''

def of_personality_type(townies, personality_type):
    # Create a list to hold the names of villagers with the specified personality type
    matching_villagers = []
    
    # Iterate through the list of Villager instances
    for villager in townies:
        # Check if the villager's personality matches the specified personality type
        if villager.personality == personality_type:
            # Add the villager's name to the list
            matching_villagers.append(villager.name)
    
    return matching_villagers

# Check
isabelle = Villager("Isabelle", "Dog", "what's up?", "Normal")
bob = Villager("Bob", "Cat", "pthhhpth","Lazy" )
stitches = Villager("Stitches", "Cub", "stuffin'","Lazy")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# Q8 ================================================================================================
'''
Buyers often look for NFTs that are closest in value to their budget. Given a sorted list of NFT values and a budget, you need to find the two NFT values that are closest to the given budget: one that is just below or equal to the budget and one that is just above or equal to the budget. If an exact match exists, it should be included as one of the values.

Write the find_closest_nft_values() function, which takes a sorted list of NFT values and a budget, and returns the pair of the two closest NFT values.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

def find_closest_nft_values(nft_values, budget):
    pass

# # Check
# nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
# nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
# nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

# print(find_closest_nft_values(nft_values, 8.0))
# print(find_closest_nft_values(nft_values_2, 6.5))
# print(find_closest_nft_values(nft_values_3, 3.0))

# Standard set v2

# Q1 ================================================================================================
'''
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Player and store it in a variable named player_one.

The Player object should have the character "Yoshi" and the kart "Super Blooper".
'''

class Player():
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

    def get_player(self):
        return f"{self.character} driving the {self.kart}"
    
    def set_character(self, name):
        # Figure out valid parameters
        if name in ("Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"):
            print("Character Updated")
            self.character = name
        else:
            print("Invalid Character")

    def add_item(self, item_name):
        if item_name in ("banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"):
            self.items.append(item_name)

    def print_inventory(self):
        count={}

        if not self.items:
            print("Inventory empty")
        else:
            for items in self.items:
                if items in count:
                    count[items]+=1
                else:
                    count[items]=1
                
            print(count)

        a="Inventory: "

        for item, num in count.items():
            a += f"{item}: {num}, "

        print(a)




player_one = Player("Yoshi", "Super Blooper")

# Check
player_one.character
player_one.kart
player_one.items

# Q1 ================================================================================================
'''
Step 1: Using the Player class from Problem 1, add the following get_player() method to your existing code:

def get_player(self):
    return f"{self.character} driving the {self.kart}"
Step 2: Create a second instance of Player in a variable named player_two.

The Player object created should have character "Bowser" and kart "Pirahna Prowler".
Step 3: Use the method get_player() below to print out "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler".
'''

player_two = Player("Bowser", "Pirahna Prowler")

# Q2 ================================================================================================

print(player_two.character, player_two.kart, player_two.items)

# Q3 ================================================================================================

player_one.kart = "Dolphin Dasher"
print(player_one.get_player())

# Q4 ================================================================================================

player_three = Player("Donkey Kong", "Standard Kart")

player_three.set_character("Peach")
print(player_three.character)
player_three.set_character("Baby Peach")
print(player_three.character)

# Q5 ================================================================================================
'''
Players can pick up special items as they race.

Update the Player class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s items attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".
'''

player_one = Player("Yoshi", "Dolphin Dasher")

print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)

# Q6 ================================================================================================
'''
Update the Player class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a player’s items list.

If the player has no items, the function should print "Inventory empty".
class Player():
    # ... methods from previous problems
    
    def print_inventory(self):
        pass
'''

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

# Q7 ================================================================================================
'''
Given a list race_results of Player objects where the first player in the list came first in the race, second player in the list came second, etc., write a function print_results() that prints the players in place.
'''

def print_results(race_results):
    # create a for loop to access the values in race_results i, player 
        # 

    for i, player in enumerate(race_results):
        print(f"{i + 1}. {player.character}")

# test
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)
# Output:
# 1. Peach
# 2. Mario
# 3. Luigi

# Q8 ================================================================================================

def get_rank(my_player):
    # create a array for order .pop(1, )
    rank = 1

    current_player = my_player


    while current_player.ahead != None:
        rank += 1
        current_player = current_player.ahead

    return rank   

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

print(get_rank(luigi))
print(get_rank(peach))
print(get_rank(mario))

# Q9 ================================================================================================
'''
Problem 9: Tom and Jerry
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create a linked list cat -> mouse where the instance cat has value "Tom" which points to the instance mouse that has value "Jerry".
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

mouse = Node("Jerry")

cat = Node("Tom")
cat.next = mouse

print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next)

# Q10 ================================================================================================
'''
In a linked list, pointers can be redirected at any place in the list.

Using the linked list from Problem 9, create a new Node dog with value "Spike" and point it to the cat node so that the full list now looks like dog -> cat -> mouse.
'''

dog = Node("Spike")
dog.next = cat

# test 
print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
# print(mouse.next.value)

