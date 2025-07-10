class SongNode:
	def __init__(self, song, artist, next=None):
          self.song = song
          self.artist = artist
          self.next = next
     
# Q3
''' Glitching out
'''

def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))

#Q4
''' Basically checking for loops in the list
'''
def on_repeat(playlist_head):
	# slow pointer -> iterate this by 1
    # fast pointer -> iterate this by 2
    # ^ fast checks everty other node, while the slow checks every node

    # while slow:
        # if slow == fast:
            # return true
        # else:
            # add 1 to slow and 2 to fast

    slow = playlist_head
    fast = playlist_head.next

    while slow:
        slow = slow.next
        fast = fast.next.next        
        if slow == fast:
            return True
    return False

# TEST
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))

#Q5 
