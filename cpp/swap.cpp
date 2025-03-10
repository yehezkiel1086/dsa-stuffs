#include <iostream>

void swap(int *a, int *b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}

int main() {
  int a = 1;
  int b = 2;

  swap(&a, &b);

  std::cout << a << " " << b << "\n";

  return 0;
}