#include <iostream>
#include <time.h>

void generateRands(int lim = 10) {
  srand(time(NULL));
  int a = rand() % lim + 1;
  int b = rand() % lim + 1;
  int c = rand() % lim + 1;

  int rands[3] = {a, b, c};

  std::cout << a << " " << b << " " << c << "\n";
}

int main() {
  // pseudo-random: not truly random (but close)
  generateRands(6);

  return 0;
}