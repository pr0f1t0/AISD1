from Lab9.graphs import *

class UnionFind:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for vertex in vertices:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    minimum_spanning_tree = []
    edges = []
    for vertex in graph:
        for neighbor in vertex.getConnections():
            weight = vertex.getWeight(neighbor)
            edges.append((vertex.getId(), neighbor.getId(), weight))

    edges.sort(key=lambda x: x[2])

    vertices = list(graph.getVertices())
    union_find = UnionFind(vertices)

    for edge in edges:
        vertex1, vertex2, weight = edge
        if union_find.find(vertex1) != union_find.find(vertex2):
            union_find.union(vertex1, vertex2)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree
