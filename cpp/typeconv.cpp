#include <iostream>

int main() {

  /**
   * type conversion = conversion a value of one data type to another
   * 
   * Implicit = automatic
   * Explicit = Precede value with new data type e.g: `(int)x`
   */

  int x = 3.14; // implicit

  std::cout << x << std::endl;

  std::cout << (char)100 << std::endl; // explicit

  return 0;
}