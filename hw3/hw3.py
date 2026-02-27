
from copy import deepcopy

def find_path(G: list[list[int]], source: int, destination: int) -> list[int] | None:
    """
    Returns any path from source to destination in a directed graph
    represented as an adjacency matrix where 0 means no edge.
    If no path exists, returns None.
    """
    # Number of vertices in the graph
    n: int = len(G)
    # visited[v] is True once vertex v has been discovered
    visited: list[bool] = [False for _ in range(n)]
    # parent[v] stores the vertex from which v was first reached
    # This will allow us to reconstruct the path later
    parent: list[int | None] = [None for _ in range(n)]
    # Stack used to implement iterative DFS
    stack: list[int] = [source]
    # Mark the start vertex as visited immediately
    visited[source] = True
    # Flag to indicate whether we have found the goal
    found: bool = False
    # Continue searching while there are vertices to explore
    # and the goal has not yet been found
    while len(stack) > 0 and not found:
        # Take the most recently added vertex (DFS behavior)
        u: int = stack.pop()
        # If we reached the goal, stop exploring
        if u == destination:
            found = True
        else:
            # Examine all possible outgoing edges u -> v
            v: int = 0
            while v < n:
                # If there is an edge from u to v
                if G[u][v] != 0:
                    # If v has not yet been visited, discover it
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = u  # record how we reached v
                        stack.append(v)  # explore v later
                v += 1
    # Prepare the result (None unless we found a path)
    path: list[int] | None = None
    # If goal was found, reconstruct the path
    if found:
        path: list[int] = []
        current: int | None = destination
        # Follow parent links backward from goal to start
        while current is not None:
            path.append(current)
            current = parent[current]
        # Reverse to obtain start -> goal order
        path.reverse()
        path = path
    return path

graph = [
    # 0   1   2   3   4
    [ 0, 10,  0,  0,  4], # 0
    [ 0,  0,  2,  0,  0], # 1
    [ 0,  0,  0, 10,  0], # 2
    [ 0,  0,  0,  0,  0], # 3
    [ 0,  0,  2,  0,  0]  # 4
]

source_vertex = 0
destination_vertex = 3
print(find_path(graph, source_vertex, destination_vertex))


def max_flow(G:list[list[int]], source:int, destination:int):
    # Shortcut to size of graph
    n = len(G)
    # Initialize return value
    f_max = 0
    # Create residual graph. Need deep copy to avoid
    # mutating the input graph G
    R = deepcopy(G)
    # Find an initial augmenting path in R
    augmenting = find_path(R)
    # While there is an augmenting path
    while augmenting is not None:
        # f_path = smallest edge of the augmenting path

        f_path = float()

        # add the path's capacity to the graph's max flow
        # Reduce capacity of forward edges in augmenting graph by f_max
        # Add reverse edges with f_max on the path
        # find the next augmenting path in R
    # Done
    return f_max