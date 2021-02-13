/**************************************************
* file: stack.c
*
* program demonstrating use of a stack
**************************************************/

#include "stack.h"

#define DEFAULT_SIZE 10

int main(int argc, char *argv[]) {
    /*  initialize stack with a random int  */
    Stack *stack = initStack(rand() % 10);

    /*  grow stack with many random ints  */
    for (int i = 1; i < DEFAULT_SIZE; i++) {
        push(&stack, rand() % 10);
    }

    printStack(stack);
    printf("\nSize of stack: %d\n", size(stack));

    /*  pop some values off the stack  */
    for (int i = 0; i < DEFAULT_SIZE / 2; i++) {
        int val = pop(&stack);
        printf("Popped %d off the stack\n", val);
    }

    printf("Size of remaining stack: %d\n", size(stack));
    printStack(stack);

    freeStack(stack);

    return 0;
}
