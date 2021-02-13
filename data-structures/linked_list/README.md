# Linked List

From [Wikipedia](https://www.wikiwand.com/en/Linked_list):

"*a linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence.

In its most basic form, each node contains: data, and a reference (in other words, a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration.*"

A chain of linked nodes, located in disparate parts of memory.

## Key Takeaways:

#### Advantages:

- List elements easily inserted or removed without reallocation (nodes need not be stored contiguously in memory / disk)

- Allow insertion and removal of nodes at any point in the list

- Insert / Remove with constant number of operations by keeping the link previous to the link being added or removed in memory during list traversal

- Can be building block for lists, stacks, queues, etc.

#### Disadvantages:

- Access time is linear

- Sequential access only, random access not feasible

- Use more memory than arrays due to storage used by node pointers

- Difficult to traverse in reverse

- Arrays have better cache locality due to contiguous memory


## Language Learning:

#### C:

###### Linked List:

- Recursively call `free()` to free entire list

- Defining new types in C containing pointers to themselves requires defining type then defining struct, called a [Forward Declaration](https://stackoverflow.com/questions/3988041/how-to-define-a-typedef-struct-containing-pointers-to-itself)

    - for example:
        ```
        typedef struct Node Node;

        struct Node {
            int val;
            Node *next;
        };
        ```

###### General:

- `abs(x)` in `<stdlib.h>` returns absolute value of int x

#### Python:

###### Linked List:

###### General:
