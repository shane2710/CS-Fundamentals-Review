/*******************************
* file: linked_list.c
*
* demo linked list usage in C
*******************************/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "linked_list.h"

#define DEFAULT_SIZE 10

int main(int argc, char *argv[]) {
    int listSize = 0;

    switch (argc) {
        case 1:
            listSize = DEFAULT_SIZE;
            break;
        case 2:
            listSize = atoi(argv[1]);
            if (!listSize) {
                printf("invalid size specified: %s\n", argv[1]);
                return 1;
            }
            break;
        default:
            printf("Usage: %s {size}\n", argv[0]);
            return 1;
    }

    /*  initialize list with single node  */
    Node *linkedList = newNode(rand() % 10, NULL);
    Node *tail = linkedList;

    /*  fill list to default size   */
    for (int i = 1; i < DEFAULT_SIZE; i++) {
        tail->next = newNode(rand() % 10, NULL);
        tail = tail->next;
    }

    printf("Default linked list size: %d\n", DEFAULT_SIZE);
    printList(linkedList);

    /*  grow / shrink list to match the specified target size   */
    int changeCount = listSize - DEFAULT_SIZE;
    if (changeCount > 0) {
        /*  add nodes   */
        printf("Added %d nodes to make list size: %d\n", changeCount, listSize);
        addNodes(linkedList, changeCount);
    } else if (changeCount < 0) {
        /*  remove nodes    */
        printf("Removed %d nodes to make list size: %d\n", abs(changeCount), listSize);
        removeNodes(linkedList, abs(changeCount));
    } else {
        /*  listSize already correct    */
        printf("Specified size is default: %d\n", DEFAULT_SIZE);
    }

    printList(linkedList);
    freeList(linkedList);

    return 0;
}
