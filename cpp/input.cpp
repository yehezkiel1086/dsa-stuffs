#include <iostream>

int main() {
  int age;
  std::string name;

  std::cout << "Enter your age: ";
  std::cin >> age;

  std::cout << "Enter your name: ";
  std::getline(std::cin >> std::ws, name); // get full line with space also eliminates any new line characters read from age input

  std::cout << "Hello " << name << std::endl;
  std::cout << "You are " << age << " years old" << std::endl;

  return 0;
}