#include <iostream>

enum Day {
  sunday = 0,
  monday = 1,
  tuesday = 2,
  wednesday = 3,
  thursday = 4,
  friday = 5,
  saturday = 6
}; // if you don't provide the values, it'll automatically assign them as above

int main() {
  /**
   * enums = a user-defined data type that consists of paired name-integer constants.
   * GREAT if you have a set of potential options
   */

  Day today = sunday;

  switch (today) {
    case sunday:
      std::cout << "It's sunday!\n";
      break;
    case monday:
      std::cout << "It's monday!\n";
      break;
    case tuesday:
      std::cout << "It's tuesday!\n";
      break;
    case wednesday:
      std::cout << "It's wednesday!\n";
      break;
    case thursday:
      std::cout << "It's thursday!\n";
      break;
    case friday:
      std::cout << "It's friday!\n";
      break;
    case saturday:
      std::cout << "It's saturday!\n";
      break;
  };

  return 0;
}