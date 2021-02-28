# Graph

[Graph](https://www.wikiwand.com/en/Graph_(abstract_data_type))

>*A graph data structure consists of a finite (and possibly mutable) set of vertices (also called nodes or points), together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as edges (also called links or lines), and for a directed graph are also known as arrows.*

[here](https://www.geeksforgeeks.org/data-structures/linked-list/).

## Key Takeaways:

- Graphs can be undirected / directed, and unweighted / weighted

#### Representations:

- Data structure relations:

Adjacency list[2]
    Vertices are stored as records or objects, and every vertex stores a list of adjacent vertices. This data structure allows the storage of additional data on the vertices. Additional data can be stored if edges are also stored as objects, in which case each vertex stores its incident edges and each edge stores its incident vertices.
Adjacency matrix[3]
    A two-dimensional matrix, in which the rows represent source vertices and columns represent destination vertices. Data on edges and vertices must be stored externally. Only the cost for one edge can be stored between each pair of vertices.


- Adjacency lists are generally preferred because they efficiently represent sparse graphs. An adjacency matrix is preferred if the graph is dense, that is the number of edges |E | is close to the number of vertices squared, |V |2, or if one must be able to quickly look up if there is an edge connecting two vertices.

#### Disadvantages:

- 


## Language Learning:

#### C:

###### Usage:

###### Graph:

###### General:

#### Python:

- This implementation uses an adjacency list

###### Usage:

`python graph.py`

###### Graph:

- 

###### General:

- Tuples are hashable to add into a set, but the order of items in the tuple matter.. the following code snippet **does not** filter out duplicate edge pairs as I first expected:

    ```python
	def getEdges(self):
        edgeset = set()
        for vert,edges in self.graph.items():
            for edge in edges:
                edgeset.add((vert, edge))

        return edgeset
	```

	returns duplicate edges:

	`{('b', 'd'), ('c', 'a'), ('b', 'a'), ('a', 'b'), ('e', 'd'), ('a', 'c'), ('c', 'd'), ('d', 'e')}`

- So, how do we create a set of vertice pairs containing unique pairs?  Well, since the vertice pairs must be unique, let's store them as sets, then form a set of these sets.

	However, sets are mutable in Python, and therefore not hashable, so [we can't nest normal sets](https://stackoverflow.com/questions/5931291/how-can-i-create-a-set-of-sets-in-python)... to work around this, declare the inner set as a [frozenset](https://docs.python.org/2/library/stdtypes.html#frozenset) which promises Python that we won't modify it and thus it becomes hashable!

	```python
	def getEdges(self):
        edgeset = set()
        for vert,edges in self.graph.items():
            for edge in edges:
                edgeset.add(frozenset({vert, edge}))

		# massage set of frozen sets into more palatable data
        return [tuple(e) for e in edgeset]
	```

	returns unique edges:

	`[('c', 'a'), ('b', 'a'), ('c', 'd'), ('b', 'd'), ('d', 'e')]`
	
