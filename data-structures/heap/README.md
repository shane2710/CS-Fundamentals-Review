# Heap

[General Heap](https://www.wikiwand.com/en/Heap_(data_structure\))
[Binary Heap](https://www.wikiwand.com/en/Binary_heap):

(The most commonly encountered heap data structure is a binary heap)

[here](https://www.geeksforgeeks.org/data-structures/linked-list/).

## Key Takeaways:

#### Advantages:

- Access `min` or `max` (depending on heap type) in `O(1)` time

- Easily sort data in place using [heapsort](TODO)


#### Disadvantages:


## Language Learning:

#### C:

###### Usage:

###### Heap:

###### General:

#### Python:

###### Usage:

`python heap.py`

###### Heap:

- Solid implementation [here](https://www.pythonpool.com/max-heap-python/)

###### General:

- Declare private data and functions with '\_' prefix:
    ```
    class Max_Heap:
		def __init__(self, arr=[]):
			self._heap = []
			
			if arr is not None:
				for root in arr:
					self.push(root)

		def _swap(L, i, j):
			L[i], L[j] = L[j], L[i]
	```
    
    In the example above, `_swap` is only available within Max_Heap internally.

