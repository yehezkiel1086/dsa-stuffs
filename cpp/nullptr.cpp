#include <iostream>

int main() {
  /**
   * Null pointer = pointer that's not pointing to anything
   * 
   * nullptr = keyword representing a null pointer literal
   * - helpful to determine if address successfully assigned to pointer
   * - be careful that your code isn't dereferencing nullptr or pointing to free memory (will cause undefined behavior)
   */

  int *ptr = nullptr;
  int x = 123;

  ptr = &x;

  if(ptr = nullptr) {
    std::cout << "not assigned.\n";
  } else {
    std::cout << "assigned.\n";
  }

  return 0;
}