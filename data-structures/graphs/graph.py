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

# note: this implementation makes it harder to remove vertices bc when
# removing associated edges, they may be stored in any place in the 
# hash table... this requires checking if every entry has the vretice
# to be removed and removing it, which is bad time complexity....
# for undirected graphs, a better appproach would be to store all edges
# for a vertice in that hash table entry, meaning redundant edge entries..
# then when deleting a vertice 'v', for each vertice it connects to 'n' forming
# an edge, remove 'v' from the edge list of 'n', then remove 'n' from the 
# edge list of 'v'... this would be better for large graphs
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
