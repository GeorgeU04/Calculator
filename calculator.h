#include <stdbool.h>
#include <stdint.h>

#ifndef CALCULATOR_H
#define CALCULATOR_H

bool is_operator(char c);
int32_t prec(char c);
bool check_input(char *str);
char *in_to_post(char *str);
int32_t eval(const char *exp);

#endif
