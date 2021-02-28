# Graph

[Graph](https://www.wikiwand.com/en/Heap_(data_structure\))

>*A excerpt here*

[here](https://www.geeksforgeeks.org/data-structures/linked-list/).

## Key Takeaways:

- 

#### Advantages:

- 

#### Disadvantages:

- 


## Language Learning:

#### C:

###### Usage:

###### Graph:

###### General:

#### Python:

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

	returns:

	`{('b', 'd'), ('c', 'a'), ('b', 'a'), ('a', 'b'), ('e', 'd'), ('a', 'c'), ('c', 'd'), ('d', 'e')}`

So, how do we create a set of vertice pairs containing unique pairs?  Well, since the vertice pairs must be unique, let's store them as sets, then form a set of these sets.

However, sets are mutable in Python, so [we can't nest normal sets](https://stackoverflow.com/questions/5931291/how-can-i-create-a-set-of-sets-in-python)... to work around this, declare the inner set as a [frozenset](https://docs.python.org/2/library/stdtypes.html#frozenset) which promises Python that we won't modify it and thus it becomes hashable!

	```python
	def getEdges(self):
        edgeset = set()
        for vert,edges in self.graph.items():
            for edge in edges:
                edgeset.add(frozenset({vert, edge}))

		# massage set of frozen sets into more palatable data
        return [tuple(e) for e in edgeset]
	```

	returns:

	`[('c', 'a'), ('b', 'a'), ('c', 'd'), ('b', 'd'), ('d', 'e')]`
	
