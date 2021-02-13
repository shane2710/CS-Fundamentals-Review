# Dynamic Array

From [Wikipedia](https://www.wikiwand.com/en/Dynamic_array):

"*a dynamic array, growable array, resizable array, dynamic table, mutable array, or array list is a random access, variable-size list data structure that allows elements to be added or removed.*"

Translation.... just any old array on the heap in C, list() in python, etc.


## Key Takeaways:

- Elements can be added at the end of a dynamic array in constant time by using the available space until this space is completely consumed

- When a dynamic array is full, and an additional element is to be added, then the underlying fixed-sized array needs to be increased in size

- Typically resizing is expensive because it involves allocating a new underlying array and copying each element from the original array.  Sometimes memory can be extended in place, but often the existing array's contents must be copied to a new, larger block of memory that is not contiguous with the original array.

- Elements can be removed from the end of a dynamic array in constant time, as no resizing is required

- The number of elements used by the dynamic array contents is its *logical size* or *size*, while the size of the underlying array is called the dynamic array's *capacity* or *physical size*, which is the maximum possible size without relocating data

## Language Learning:

#### C:

- An array declared w/ fixed length is allocated on the stack and cannot
  be dynamically resized

- Dynamic arrays are allocated at runtime on the heap via malloc() or similar
  calls, and must be freed manually once their scope has run its course

- Resizing a dynamic array with realloc() may return a pointer to a completely
  new starting memory address for the array, meaning the memory was copied to a
  larger block (expensive!)

#### Python:

- Lists are dynamic arrays....

