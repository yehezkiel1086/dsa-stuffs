#include <iostream>
#include <vector>

typedef std::vector<std::pair<std::string, int>> pairlist_t;

// typedef std::string text_t;
// typedef int number_t;

using text_t = std::string;
using number_t = int;

int main() {
  /**
   * typedef = reserved keyword used to create an additional name (alias) for another data type. New identifier for an existing type helps with readability and reduces typos.
   * 
   * Use when there is a clear benefit replaced with 'using' (work better w/ templates)
   */

  text_t name = "John";
  number_t age = 25;

  std::cout << "Name: " << name << std::endl;
  std::cout << "Age: " << age << std::endl;

  return 0;
}