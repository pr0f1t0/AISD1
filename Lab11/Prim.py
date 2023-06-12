import heapq
from Lab9.graphs import *

def prim(graph):
    minimum_spanning_tree = []
    start_vertex = next(iter(graph))
    visited = set([start_vertex])
    edges = [(weight, start_vertex, neighbor) for neighbor, weight in start_vertex.connectedTo.items()]
    heapq.heapify(edges)

    while edges:
        weight, current_vertex, next_vertex = heapq.heappop(edges)
        if next_vertex not in visited:
            visited.add(next_vertex)
            minimum_spanning_tree.append((current_vertex.getId(), next_vertex.getId(), weight))
            for neighbor, weight in next_vertex.connectedTo.items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, next_vertex, neighbor))

    return minimum_spanning_tree
