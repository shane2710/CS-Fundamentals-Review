# Heap

[General Heap](https://www.wikiwand.com/en/Heap_(data_structure\))
[Binary Heap](https://www.wikiwand.com/en/Binary_heap):

>*A heap is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C.*

(The most commonly encountered heap data structure is a binary heap)

[here](https://www.geeksforgeeks.org/data-structures/linked-list/).

## Key Takeaways:

- The highest (or lowest) priority element is always stored at the root

- Not sorted, but partially ordered data structure

- Binary heap easily stored in mem as an array

#### Advantages:

- Access `min` or `max` (depending on heap type) in `O(1)` time

- Easily sort data in place using [heapsort](TODO) for O(n) memory use

#### Disadvantages:

- No traversals possible (compared to binary search trees, arrays, linked
  lists)

- Refactoring in accordance w/ heap property, aka `heapify()` must be called on
  each added or removed node


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

    ```python
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

