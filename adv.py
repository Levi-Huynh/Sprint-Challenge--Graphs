from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

"""
Understand 
-Given a undirected, cyclic, connected graph
-Nodes are rooms
-Edges are room exits/connections
-500 nodes

-Output a traversal path of shortest number of directions that visits every room
(total directions/moves should be <2000)

-Must be able to go backwards if hit room with dead end
-Helper functions to find the exits in the room & the rooms they connect to


Plan:
-Use BFS to find shortest path to the next room where the exits =? / unexplored
-Create a visited_room dict that stores our room-id as key & a sub dictionary as its value
    -subdictionary should have all the possible exits as keys & value should be the new rooms conected
    -use a helper 'log_new_room' to do this for us, using 'get_exits' to return possible exits 
    
-Create a main while loop that continues but breaks when the len of visited rooms > len of room_graphs
    (we only need to visit every room & store that in our visited_room dict)
-Inside While loop:
    -Check if the current room id is a key in our visited_room dict
    -Use helper function to add the room to dict (`get_exits method from room class`) if its not
    -Iterate through each exit in the current room & store the exits that are unexplored / have value
    of '?' inside an empty list (room_exits)
    -If the len of our unexplored exits (room_exits) for curr room is 0:
        -use our BFS to return the next path of rooms from our QUEUE that have unexplored exits
            -iterate through the room_ids from our returned path coming from BFS
            -for all the exits in our current room, verify the room_ids in the path exist for curr_room
            -if so append that exit direction to our traversal_path
            -Log the new room id, as the value for that exit direction in our current room (using get_room_in_direction room class method)
            -log the new room id as a key, if its not yet logged in our visited_room dict
            -Log our current room, as the room value for the opposite direction, for our new room key in the visited_rooms dict
            -travel to the exit direction using player.travel
    -Else if the len of our unexplored exits (room_exits) is > 0 (we have unexplored exits for our current room)
        -randomly choose an exit from our room_exits (use random.choice)
        -travel to that randomly choosen exit using player.travel
        -use helper function `get_room_in_direction` to log the new rooms, for the randomly choosen exit of our curr room
        -log the new room to visited_rooms dict , and for the opposite direction (randomly chosen exit), log the current_room as the value 
        -travel to our randomly chosen exit 
"""

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
