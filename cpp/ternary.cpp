#include <iostream>

int main() {
  int grade = 60;
  bool pass = grade >= 65? true: false;
  bool even = grade % 2 == 0? true: false;

  if(pass)
    std::cout << "You pass.\n";
  else
    std::cout << "You fail.\n";

  if(even)
    std::cout << "Your grade is even.\n";
  else
  std::cout << "Your grade is odd.\n";

  return 0;
}