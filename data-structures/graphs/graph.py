#!/usr/bin/python

class Graph:
    def __init__(self, gdict=None):
        if (gdict):
            self.graph = gdict
        else:
            self.graph = {}

    def getVertices(self):
        return [v for v in self.graph.keys()]

    def getEdges(self):
        edgeset = set()
        for vert,edges in self.graph.items():
            for edge in edges:
                edgeset.add(frozenset({vert, edge}))

        return [tuple(e) for e in edgeset]

    def addVertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []

    def addEdge(self, edge):
        self.graph[edge.pop()].add(edge.pop())

gdict = { "a" : {"b","c"},
          "b" : {"a", "d"},
          "c" : {"a", "d"},
          "d" : {"e"},
          "e" : {"d"}
        }

g = Graph(gdict)
print(g.getVertices())
print(g.getEdges())
g.addVertex("f")
g.addEdge({"f","e"})
g.addEdge({"b","e"})
g.addEdge({"b","d"})
print(g.getVertices())
print(g.getEdges())
