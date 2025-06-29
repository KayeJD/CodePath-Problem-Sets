# Standard set 1 \

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
    pass

# Check
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
