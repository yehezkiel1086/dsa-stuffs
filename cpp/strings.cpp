#include <iostream>

int main() {
  std::string name;

  std::cout << "Enter your name: ";
  std::getline(std::cin, name);

  if(name.length() > 12) {
    std::cout << "Your name can't be over 12 chars!\n";
  } else if(name.empty()) {
    std::cout << "You didn't enter your name!\n";
  } else {
    std::cout << "Welcome, " << name << "!\n";
  }

  int i = name.find(' ');

  name.erase(i, name.length());

  name.insert(name.length(), "@");

  name.append("gmail.com");

  std::cout << "Your username is now: " << name << "\n";

  char init = name.at(0);

  std::cout << "Your name initial: " << init << "\n";

  name.clear();

  std::cout << "Your name is cleared: " << name << "\n";

  return 0;
}