/**************************************************
* file: linked_list.h
*
* header file containing implementation details
* for a linked list
**************************************************/
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

typedef struct Node Node;

struct Node {
    int val;
    Node *next;
};


/* pretty print linked list contents    */
void printList(Node *head) {
    Node *curr = head;
    printf("\n");
    while (curr) {
        printf("%d -> ", curr->val);
        curr = curr->next;
    }
    printf("NULL\n");
}


/*  allocate and return a new Node  */
Node *newNode(int val, Node *next) {
    Node *node = malloc(sizeof(Node));
    assert(node);
    node->val = val;
    node->next = next;
    return node;
}


/*  free linked list    */
void freeList(Node *list) {
    if (list->next) {
        freeList(list->next);
    }
    free(list);
}


/*  add specified number of nodes to list   */
void addNodes(Node *head, int nodeCount) {
    Node *tail = head;
    while (tail->next) {
        tail = tail->next;
    }
    for (int i = 0; i < nodeCount; i++) {
        tail->next = newNode(rand() % 10, NULL);
        tail = tail->next;
    }
}


/*  recursively remove specified number of nodes from list    */
int removeNodes(Node *head, int nodeCount) {
    if (head) {
        int remove = removeNodes(head->next, nodeCount);
        if (remove > 1) {
            free(head);
            return --remove;
        } else if (remove == 1) {
            head->next = NULL;
            return 0;
        } else {
            return 0;
        }
    } else {
        return nodeCount + 1;
    }
}


