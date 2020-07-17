from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# -------WORLD MAP CONNECTIONS ---------------
# print("Is this the WORLD?", room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
print("TYPE of room", type(room_graph[0][1]))

# start by initiating empty list of movements to keep track
# Stack, rooms visited, returning to same room, and full map object.
def traverse_adv():
    stack = []
    visited = []
    go_back = []
    world_map = {}
    # print("first room", player.current_room.id)

    #find first room... 
    #put it in the stack
    first = player.current_room.id
    stack.append(first)

    #keep track of current room
    #visit room if not in visited 
    # find the exits (get)
    # populate exits on world map current : {n: "?"}
    # Choose an exit, first key with value == "?"
    # Travel to next room through that exit -- "n"
    #Create logic to discover the opposite of exit
    # Update path with exit coordinate
    # Update world ----> current: {n: 1}
    #Create next entry for the "next room", where we are now
    # world : {0:{n:1...}, 1:{s:0}}     n is the exit and s is the opposite

    # append "next room" to stack
    # begin loop again
    while len(visited) != len(room_graph):
        found = "nothing"
        print("found", found)

        #Pop + set to current
        current = stack.pop()

        #find exits
        exits = player.current_room.get_exits()
        print("current room: ", current, "exit directions: ", exits)

        #check if its been visited
        if current not in visited:
            visited.append(current)
            print("visited rooms: ", visited)

        #ADD TO BACK TRACK list!!! 
        go_back.append(current)
        print("backtracked list: ", go_back)

        #Use Enumerate: It allows us to loop over something and have an automatic counter. 
        #add entryway
        if current not in world_map:
            world_map[current] = {i[1] : "?" for i in enumerate(exits)}
        print("my world: ", world_map)



traverse_adv()
print("ADVENTURE LENGTH: ", len(traversal_path))

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
