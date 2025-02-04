#include <stdlib.h>
#include <iostream>

using namespace std;

#define MAX 10;
int size = 0;

struct stack {
  int items[MAX];
  int top;
};
typedef struct stack st;
