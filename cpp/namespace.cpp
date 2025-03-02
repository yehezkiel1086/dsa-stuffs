#include <iostream>

namespace first {
  int x = 1;
}

namespace second {
  int x = 2;
}

int main() {
  /**
   * Namespace:
   * - Solution for preventing name conflicts in large projects. 
   * - Each entity needs unique name. 
   * - A namespace allows for identically named entities as long as the namespaces are different.
   */

  std::cout << "first: " << first::x << "\n";
  std::cout << "second: " << second::x << "\n";

  using namespace first;

  std::cout << "first: " << x << "\n";

  // instead of this:
  // using namespace std;
  // the following is better:
  using std::cout;
  using std::string;

  string name = "Brian";

  cout << "Name: " << name << "\n";

  return 0;
}