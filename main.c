#include "calculator.h"
#include "stack.h"
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
 * Add basic GUI
 * Add negative integer support
 * Add floating point implementation
 * Add exponents
 * ...
 */

int32_t get_input() {
  char *input = (char *)malloc(64 * sizeof(char));
  if (input == NULL) {
    fprintf(stderr, "ERROR Memory Allocation Failed");
    exit(EXIT_FAILURE);
  }
  while (1) {
    printf("Input an expression ('q' to exit): ");
    if (fgets(input, 64, stdin) == NULL) {
      fprintf(stderr, "[ERROR] Input could not be processed\n");
      free(input);
      exit(EXIT_FAILURE);
    }
    if (input[0] == 'q')
      break;

    if (check_input(input)) {
      fprintf(stderr, "[ERROR] Invalid input\n");
      continue;
    }

    char *postfix = in_to_post(input);
    int32_t answer = eval(postfix);
    printf("Post Fix: %s\n", postfix);
    printf("Your answer is %d\n", answer);

    free(postfix);
  }
  printf("Thanks for using my calculator!!\n");
  free(input);
  return 0;
}

int main(int argc, char *argv[]) {

  get_input();

  return 0;
}
