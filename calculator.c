#include "calculator.h"
#include "stack.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * TODO
 * Making somewhat functional: DONE
 * Input error handling: DONE
 * Add larger digit implementation: DONE
 * Add basic GUI DONE
 * Add negative integer support
 * Add floating point implementation
 * Add exponents
 * ...
 */

bool is_operator(char c) {
  char ops[] = {'+', '-', '/', '*'};
  for (size_t i = 0; i < sizeof(ops) / sizeof(ops[0]); ++i) {
    if (c == ops[i])
      return true;
  }
  return false;
}

int32_t prec(char c) {
  if (c == '/' || c == '*')
    return 2;
  else if (c == '+' || c == '-')
    return 1;
  else
    return -1;
}

int32_t eval(const char *exp) {
  Stack *stack = create_stack(strlen(exp));
  if (!stack) {
    fprintf(stderr, "ERROR Memory Allocation Error");
    exit(EXIT_FAILURE);
  }
  for (size_t i = 0; exp[i]; ++i) {
    if (exp[i] == ' ' || exp[i] == '\n')
      continue;

    else if (isdigit(exp[i])) {
      int32_t num = 0;

      while (isdigit(exp[i])) {
        // deal with the multiple digit numbers
        num = num * 10 + (int32_t)(exp[i] - '0');
        ++i;
      }
      --i;

      push(stack, num);
    }

    else {
      int32_t num1 = pop(stack);
      int32_t num2 = pop(stack);

      switch (exp[i]) {
      case '+':
        push(stack, num2 + num1);
        break;
      case '-':
        push(stack, num2 - num1);
        break;
      case '*':
        push(stack, num2 * num1);
        break;
      case '/':
        push(stack, num2 / num1);
        break;
      default:
        fprintf(stderr, "ERROR: Unknown operator encountered: %c\n", exp[i]);
        free_stack(stack);
        exit(EXIT_FAILURE);
      }
    }
  }
  int32_t result = pop(stack);
  free(stack);
  return result;
}

char *in_to_post(char *str) {
  char *output = (char *)malloc((strlen(str) * 2 + 1) * sizeof(char));
  if (output == NULL) {
    fprintf(stderr, "ERROR: Memory Allocation Failed");
    exit(EXIT_FAILURE);
  }

  Stack *stack = create_stack(64);
  size_t j = -1;
  for (size_t i = 0; i < strlen(str); ++i) {
    if (isdigit(str[i])) { // operand
      output[++j] = str[i];
      if (i < strlen(str) - 1 && !isdigit(str[i + 1])) // Check for operand
        output[++j] = ' ';
    } else if (str[i] == '(') { // left paren
      push(stack, str[i]);
    } else if (str[i] == ')') { // right paren
      while (peek(stack) != '(') {
        output[++j] = ' ';
        output[++j] = pop(stack);
      }
      pop(stack); // Discard the left paren
    } else {      // operator
      while (!is_empty(stack) && prec(str[i]) <= prec(peek(stack))) {
        output[++j] = pop(stack);
      }
      push(stack, str[i]);
    }
  }
  while (!is_empty(stack)) {
    output[++j] = ' ';
    output[++j] = pop(stack);
  }
  output[++j] = '\0';
  free_stack(stack);

  return output;
}

bool check_input(char *str) {
  for (size_t i = 0; i < strlen(str); ++i) {
    if (str[i] == '\n')
      continue;

    if (!isdigit(str[i]) && !is_operator(str[i]) && str[i] != ')' &&
        str[i] != '(') {
      printf("Character '%c' (%d) is not recognized\n", str[i], (int)str[i]);
      return true;
    }
  }
  return false;
}
