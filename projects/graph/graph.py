"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        Return all as a SET

        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #Make Queue
        q = Queue()
        # enquenue our starting node
        q.enqueue(starting_vertex)

        #make a set to track if we've been here before
        passed = set()

        #While our queue isn't empty
        while q.size() > 0:
        ##  dequeue whatever is @ front of the line (current_node)
            current_node = q.dequeue()
        ## if we haven't passed over this node yet
            if current_node not in passed:
            ##  mark as passed
                passed.add(current_node)
            ##  gets its neighbors
            ## 
                neighbors = self.get_neighbors(current_node)
            ##  for each of the neighbors, 
                for neighbor in neighbors:
                ## add to queue
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        ===== DFS =====
        """
    ## Create a stack
        s = Stack()
    #1. Starting Node + Target Node
    # 2. Add [starting_node] to path, and push it to stack
        s.push(starting_vertex)
    ## make a set to track if we've been here before
        passed = set()
    ## while our stack isn't empty
        while s.size():
        # 3. pop last item from stack (current node)
            current_node = s.pop()
        ## if we haven't visited this vertex before...
            if current_node not in passed:
            ## run function / print
                print(current_node)
            ## mark as passed
                passed.add(current_node)
            ## get its neighbors
                neighbors = self.get_neighbors(current_node)
            # 4. check the last item in the path, for instance [1, 2, 4, 6, 7]... check 7 (path[-1])
            # 5. add path[-1] to your visited
            # 6. get neighbors of path[-1]
            # 7. add to your path, so for each neighbor, create a path copy, add the neighbor to end of path
            #for each neighbor
                for neighbor in neighbors:
            # 8. push your new path to your stack
                    s.push(neighbor)
            # 9. for instance, if neighbors of 7 are 10, 12, 13, 6, but 6 has been visited
            # 10. [1, 2, 4, 6, 7, 10], [1, 2, 4, 6, 7, 12], [1, 2, 4, 6, 7, 13] will be added to stack
            # 11. when path[-1] is your target, stop and return the path


    def dft_recursive(self, starting_vertex, passed=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # mark this vertex as passed
        passed.add(starting_vertex)
        print(starting_vertex)
        #for each neighbor
        neighbors = self.get_neighbors(starting_vertex)

        # if len(neighbors) == 0:
        #     return

        for neighbor in neighbors:
        ## if its not passed
            if neighbor not in passed:
            ## recurse on the neighbor
                self.dft_recursive(neighbor, passed)
        
        # return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #start with a queue
        q = Queue()
        # make a set to track if it's passed
        passed = set()

        path = [starting_vertex]
        q.enqueue(path)

        # go to node and find if it's in the graph or not
        #while q isnt empty
        while q.size():
        #dequeue path at front of line (starting_v)
            current_path = q.dequeue()
            #need id of node
            current_node = current_path[-1]

        ##  if this node is targt node (destination_v)
            if current_node == destination_vertex:
        # return True (current_path because we want to return a list)
                return current_path

        ## if not passed:
            if current_node not in passed:
            #mark as passed
                passed.add(current_node)
            # get neighbors
                neighbors = self.get_neighbors(current_node)
            # for each neighbor
                for neighbor in neighbors:

            # add to q
                    q.enqueue(current_path + [neighbor])



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
