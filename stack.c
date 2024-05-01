#include "stack.h"
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct Stack {
  int32_t top;       // top of stack
  int32_t *array;    // the array which holds the contents
  uint32_t capacity; // how many items it can hold
  uint32_t size;     // current element amount in stack
};

// creates the stack
Stack *create_stack(int32_t capacity) {
  Stack *stack = (Stack *)malloc(sizeof(Stack));
  if (stack == NULL) {
    fprintf(stderr, "ERROR: Memory Allocation Failed.\n");
    exit(EXIT_FAILURE);
  }
  stack->top = -1;
  stack->capacity = capacity;
  stack->size = 0;
  stack->array = (int32_t *)malloc(sizeof(int32_t) * stack->capacity);
  if (stack->array == NULL) {
    fprintf(stderr, "ERROR: Memory Allocation Failed.\n");
    free(stack);
    exit(EXIT_FAILURE);
  }
  return stack;
}

// pushes a value onto the stack and resizes it if it is at capacity
void push(Stack *stack, int32_t value) {
  if (stack->top == stack->capacity - 1) {
    stack->capacity += 10;
    int32_t *temp =
        (int32_t *)realloc(stack->array, sizeof(int32_t) * stack->capacity);
    if (temp == NULL) {
      fprintf(stderr, "ERROR: Memory Allocation Failed.\n");
      return;
    }
    stack->array = temp;
  }
  stack->size++;
  stack->array[++stack->top] = value;
}

// pops an item off the top of the stack and returns it
int32_t pop(Stack *stack) {
  if (is_empty(stack)) {
    return '@';
  }
  return stack->array[stack->top--];
}

// checks if the stack is empty
bool is_empty(Stack *stack) { return stack->top == -1; }

// returns the item at the top of the stack without removing it
int32_t peek(Stack *stack) {
  if (is_empty(stack)) {
    return '@';
  }
  return stack->array[stack->top];
}

// returns stack size
int32_t stack_size(Stack *stack) { return stack->size; }

// frees the stack and its array
void free_stack(Stack *stack) {
  free(stack->array);
  free(stack);
}
