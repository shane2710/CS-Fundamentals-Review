/**************************************************
* file: queue.h
*
* header file containing implementation details
* for a queue based on a linked list
**************************************************/

#include "linked_list.h"

typedef struct Queue Queue;

struct Queue {
    Node *head;
    Node *tail;
}

Queue *initQueue() {
    Queue *q = malloc(sizeof(Queue));
    assert(q);
    return q;
}
