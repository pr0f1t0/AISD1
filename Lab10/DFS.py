from Lab9.graphs import *


def dfs(graph):
    for vertex in graph.getVertices():
        vertex.p = -1
        vertex.visited = False

    time = 0

    for vertex in graph.getVertices():
        if not vertex.visited:
            time = dfs_explore(vertex, time)


def dfs_explore(vertex, time):
    time += 1
    vertex.time_1 = time
    vertex.visited = True

    for neighbor in vertex.getConnections():
        if not neighbor.visited:
            neighbor.p = vertex
            time = dfs_explore(neighbor, time)

    time += 1
    vertex.time_2 = time

    return time




