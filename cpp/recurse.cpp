#include <iostream>

int factorial(int n);

int main() {
  /**
   * recursion = a programming technique where a function invokes itself from within, break a complex concept into a repeatable single steps
   * 
   * (iterative vs recursive)
   * - advantages = less code and cleaner, useful for sorting and searching algos
   * - disadvantages = uses more memory, slower
   */

  int result = factorial(10);

  std::cout << "Factorial: " << result << "\n";

  return 0;
}

int factorial(int n) {
  if (n == 1) return n;
  return factorial(n - 1) * n;
}