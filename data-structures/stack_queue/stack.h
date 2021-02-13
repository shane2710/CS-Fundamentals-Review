/**************************************************
* file: stack.h
*
* header file containing implementation details
* for a stack based on a linked list
**************************************************/

#include "linked_list.h"

typedef Node Stack;

Stack *initStack(int val) {
    Stack *stack = malloc(sizeof(Stack));
    assert(stack);
    stack->val = val;
    stack->next = NULL;
    return stack;
}

void push(Stack **stack, int val) {
    Node *node = newNode(val, *stack);
    *stack = node;
}

int pop(Stack **stack) {
    Stack *tmp = *stack;
    int val = (*stack)->val;
    *stack = (*stack)->next;
    free(tmp);
    return val;
}

void printStack(Stack *stack) {
    printList((Node *)stack);
}

void freeStack(Stack *stack) {
    if (stack)
        freeList((Node *)stack);
}

int size(Stack *stack) {
    int size = 0;
    while (stack) {
        size++;
        stack = stack->next;
    }
    return size;
}
