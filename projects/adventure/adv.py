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

# opposites = { 'n': 's', 'e': 'w', 'w': 'e', 's': 'n' }

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


    # Update path with exit coordinate
    # Update world ----> current: {n: 1}
    #Create next entry for the "next room", where we are now
    # world : {0:{n:1...}, 1:{s:0}}     n is the exit and s is the opposite
    # Choose an exit, first key with value == "?"
    # Travel to next room through that exit -- "n"
    #Create logic to discover the opposite of exit


    #pick first exit w value "?" -> from world_map
    for item in world_map[current].items():
        print("items IS", item)

        if item[1] == '?':
            found = 'found'
            exit = item[0]
            print("exit item: ", exit)

            if exit == "n":
                opposite = "s",
            if exit == "s":
                opposite = "n",
            if exit == "e":
                opposite = "w",
            if exit == "w":
                opposite = "e"
            break
    if found == "found":
        pass


    else:
        print("Not a ?")
        print("go_back list", go_back)

        #no ?, go back
        value = go_back.pop()
        before = go_back.pop()
        print("current room: ", value, "before: ", before)

        for key in world_map[value]:
            print("my 🔑", key)
            if world_map[value][key] == before:
                exit = key



        #logic to discover opposite
        if exit == "n" :
            opposite = "s"
        if exit == "s" :
            opposite = "n"
        if exit == "e" :
            opposite = "w"
        if exit == "w" :
            opposite = "e"
        
        #print("breaking")
        #print("exit is", exit)

        #travel
        #print("current room is", current)
        player.travel(exit)
        next_room = player.current_room.id
        #print("about to travel from room ", current, exit, "to", next_room)

        #update my exits
        exits = player.current_room.get_exits()
        #print("new exits", exits)

        #print("exit was ", exit)
        #print("opposite is", opposite)

        #add coordinate to path  
        traversal_path.append(exit)
        #print("path", traversal_path)

        #update current entry in map
        
        if world_map[current][exit] != '?':
            pass
            #print("do nothing")
        else:
            world_map[current].update({exit:next_room})
        
        #add next entry to my map 
        #get exits
        #exits = player.current_room.get_exits()
        #print("exits from room", next_room , exits)

        #Add entry
        if next_room in world_map:
            pass
            #print(next_room, "  already in world") 
        else:
            world_map[next_room] = {i[1]: "?" for i in enumerate(exits)}

        #print("whats this", world_map[next_room][opposite])
        if  world_map[next_room][opposite] is True and world_map[next_room][opposite] != "?":
            pass
            #print("DONT UPDATE WORLD")
        else:
            #print("UPDATING")
            world_map[next_room].update({opposite:current})
        #print("my world_map", world_map)

        #Add next_room to stack to explore in next iteration
        stack.append(next_room)


        #print("world now", world_map)

        
            
        

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


    # #print("traversal path right now", traversal_path)
    # print("current room is ", player.current_room.id)
    # #keep track of visited node, has to be len of 500
    # visited = []
    # stack = []
    # count = 0
    # directions = ["n", "e", "s", "w"]
    # direction = directions[count]
    
    # prev_room = player.current_room.id
    # stack.append(player.current_room.id)
    
    # #while len(visited) != len(world_map):
    # for i in range(30):
    #     print("LEN VISITED", len(visited))
    #     print("LEN WORLD", len(world_map))
    
    #     print("enter main loop")
    #     print("MAIN DIRECTION", direction)
    #     room = stack.pop()
    #     print("room is", room)

    #     #check if it's on visited
    #     if room not in visited:
    #         print("visiting room ", room)
    #         visited.append(room)
    #     print("visited", visited)
    
    
    #     if direction == "n":
    #         opposite = "s"
    #     if direction == "s":
    #         opposite = "n"
    #     if direction == "e":
    #         opposite = "w"
    #     if direction == "w":
    #         opposite = "e" 

    #     proom = player.current_room.id
    #     print("prev room is ", proom)
    #     print("travelinnggg", direction)
    #     player.travel(direction)
    #     print("current", player.current_room.id)

    #     if proom != player.current_room.id: 

    #         print("different rooms, update map")


    #     #Loop until player can move
    #     while proom == player.current_room.id:
    #         count += 1
    #         print("in the same room")
    #         if count > 3:
    #             print("count is too high, resetting")
    #             count = 0
    #         else:

    #             print("count is cool")
    #         print("COUNT", count)
    #         direction = directions[count]
    #         print("direction is ", direction)
    #         player.travel(direction)
    #         if direction == "n":
    #             opposite = "s"
    #         if direction == "s":
    #             opposite = "n"
    #         if direction == "e":
    #             opposite = "w"
    #         if direction == "w":
    #             opposite = "e"

    #     world_map[proom][direction] = player.current_room.id
    #     world_map[player.current_room.id][opposite] = proom
    #     print("out of the loop!!")
    #     print("map now", world_map)
    #     print("now in room", player.current_room.id)

    #     stack.append(player.current_room.id)
    #     traversal_path.append(direction)
    #     print("traversal_path", traversal_path)