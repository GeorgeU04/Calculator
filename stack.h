#include <stdbool.h>
#include <stdint.h>

#ifndef STACK_H
#define STACK_H

struct Stack typedef Stack;

Stack *create_stack(int32_t capacity);
void push(Stack *stack, int32_t value);
int32_t pop(Stack *stack);
bool is_empty(Stack *stack);
int32_t peek(Stack *stack);
void free_stack(Stack *stack);
int32_t stack_size(Stack *stack);
#endif
