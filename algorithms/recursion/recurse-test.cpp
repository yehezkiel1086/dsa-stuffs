#include <iostream>
#include <math.h>

int recursiveSum(int n) {
  if (n == 1)
    return 1;
  return n + recursiveSum(n - 1);
}

int evenSquares(int n) {
  if (n == 1)
    return 0;
  else if (n % 2 == 0)
    return pow(n, 2) + evenSquares(n - 1);
  return evenSquares(n - 1);
}

bool linear(std::string str, char c, int l) {
  if (l < 0)
    return 0;
  else if (str[l] == c)
    return 1;
  return linear(str, c, l - 1);
}

int main() {
  int sum = recursiveSum(5);
  int eSquares = evenSquares(5);
  bool contH = linear("chicago", 'h', 7);

  std::cout << "sum of 1-5: " << sum << std::endl;
  std::cout << "even squares of 1-5: " << eSquares << std::endl;
  std::cout << "contains h: " << contH << std::endl;
  return 0;
}