#include <iostream>

int main() {
  /**
   * array = data structure that could hold multiple values
   * - values of array are accessed by an index number
   * - "kind of like a variable that holds multiple values"
   */
  std::string cars[] = {"Toyota", "Mitsubishi", "Nissan"};

  std::cout << cars[0] << " " << cars[1] << " " << cars[2] << "\n";

  return 0;
}