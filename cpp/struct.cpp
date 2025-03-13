#include <iostream>

struct student {
  std::string name;
  double gpa;
  bool enrolled = false;
};

int main() {
  /**
   * struct = A structure that group related variables under one name
   * - structs can contain many different data types (string, int, dobule, bool, etc)
   * - vars in a struct are known as "members"
   * - members can be accessed with . "Class member access operator"
   */
  student std1;
  std1.name = "Spongebob";
  std1.gpa = 3.2;
  std1.enrolled = true;

  student std2;
  std2.name = "Patrick";
  std2.gpa = 2.8;
  std2.enrolled = true;

  std::cout << std1.name << "\n";
  std::cout << std1.gpa << "\n";
  std::cout << std1.enrolled << "\n";

  std::cout << std2.name << "\n";
  std::cout << std2.gpa << "\n";
  std::cout << std2.enrolled << "\n";

  return 0;
}