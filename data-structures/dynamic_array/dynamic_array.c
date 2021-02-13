/*******************************
* file: dynamic_array.c
*
* demo dynamic array usage in C
*
*******************************/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define DEFAULT_SIZE 10
#define LINE_WRAP 10

void printArray(int *array, int size) {
    printf("\n");
    for (int i = 0; i <= (size / LINE_WRAP); i++) {
        for (int j = 0; j < LINE_WRAP; j++) {
            if (i*10 + j > size-1)
                break;
            printf("%d\t", array[i+j]);
        }
        printf("\n\n");
    }
}

int main(int argc, char *argv[]) {
    int arraySize = 0;

    switch (argc) {
        case 1:
            arraySize = DEFAULT_SIZE;
            break;
        case 2:
            arraySize = atoi(argv[1]);
            if (!arraySize) {
                printf("invalid size specified: %s\n", argv[1]);
                return 1;
            }
            break;
        default:
            printf("Usage: %s {size}\n", argv[0]);
            return 1;
    }

    /* allocate an array of ints on the heap and dynamically resize */
    int *dynamicArray = malloc(sizeof(int)*DEFAULT_SIZE);
    assert(dynamicArray);

    for (int i = 0; i < DEFAULT_SIZE; i++) {
        dynamicArray[i] = rand() % 20;
    }

    printf("Current size of dynamic array:\t%d\n", DEFAULT_SIZE);
    printArray(dynamicArray, DEFAULT_SIZE);

    /* reallocate to target size and fill remainder of space   */
    dynamicArray = realloc(dynamicArray, sizeof(int)*arraySize);
    assert(dynamicArray);

    for (int i = DEFAULT_SIZE; i < arraySize; i++) {
        dynamicArray[i] = rand() % 20;
    }

    printf("New size of dynamic array:\t%d\n", arraySize);
    printArray(dynamicArray, arraySize);

    /* free memory used by array since it was allocated at runtime on heap */
    free(dynamicArray);

    return 0;
}
