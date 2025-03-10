#include <iostream>

void printName(std::string name);
int add(int a, int b);

int main() {
  // function: a block of reusable code

  std::string name = "Yehezkiel";
  printName(name);
  int res = add(1, 2);

  std::cout << "Result: " << res << "\n";

  return 0;
}

void printName(std::string name) {
  std::cout << "Name: " << name << "\n";
}

int add(int a, int b) {
  return a + b;
}