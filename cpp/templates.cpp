#include <iostream>
template <typename T>

T max(T a, T b) {
  return a > b ? a: b;
}

int main() {
  std::cout << max('a', 'z') << "\n";
  std::cout << max(1000, -1) << "\n";
  return 0;
}