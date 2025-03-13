#include <iostream>
template <typename T, typename U>

T max(T a, U b) {
  return a > b ? a: b;
}

int main() {
  std::cout << max('a', 'z') << "\n";
  std::cout << max(1000, -1.2) << "\n";
  return 0;
}