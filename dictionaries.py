# # STANDARD SET #####################################################################################################
# def lineup(artists, set_times):
#     """
#     Create a dictionary mapping artists to their set times.
    
#     :param artists: List of artist names.
#     :param set_times: List of set times corresponding to the artists.
#     :return: Dictionary mapping each artist to their set time.
#     """

#     artistsAndTimes = {}

#     if len(artists) != len(set_times):
#         return []
    
#     for i, artist in enumerate(artists):
#         if artist not in artistsAndTimes:
#             artistsAndTimes[artist] = set_times[i]

#     return artistsAndTimes

    
# def test_lineup():
#     assert lineup(["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"], ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]) == {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalia": "7:30 PM"}


# if __name__ == "__main__":
#     test_lineup()
#     print("All tests passed!")


# Advanced Problem Set Version 1

# Q1
''' Problem 1: Counting Treasure
Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

Example Output:

15
50
'''

def total_treasures(treasure_map):
    # go through all .values() and return a sum value

    sum = 0

    for treasures in treasure_map.values():
        sum += treasures

    return sum

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 

# Q2
''' Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.
'''

def can_trust_message(message):
    # create letters = 0

    #for loop: iterate through all chars in the string
        # if not ' ':
            #turn the char to lower case
            # check if char in seen set
            # if no, letters++

    # if letters >= 26: return true

    letters = 0
    seen = set()

    for char in message:
        if char != ' ': 
            char = char.lower()
            if char not in seen:
                seen.add(char)
                letters += 1

    if letters >= 26:
        return True
    return False

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

# Example Output:

# True
# False

# Q3
''' Problem 3: Find All Duplicate Treasure Chests in an Array
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.
'''

def find_duplicate_chests(chests):
    # create dup dict
    # creat ans list

    # for loop: iterate thru all chests
        # if chest not in dup: dup[chest] = 1
        # else: dup[chest] += 1

    # for loop: chest in dup.keys()
        # if dup[chest] >= 2:
            # append chest to ans 

    # return ans

    dup = {}
    ans = []

    for chest in chests:
        if chest not in dup:
            dup[chest] = 1
        else:
            dup[chest] += 1

    for chest in dup.keys():
        if dup[chest] >= 2:
            ans.append(chest)
    
    return ans


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

# Example Output:

# [2, 3]
# [1]
# []