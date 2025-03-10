#include <iostream>

int main() {
  /**
   * sizeof() = determines the size of a: variable, data type, class, object, etc
   */
  
  double gpa = 3.4;
  std::string name = "Yehezkiel Wiradhika";
  char grade = 'A';
  bool isStudent = true;
  int nums[] = {1, 2, 3, 4, 5, 6};
  std::string students[] = {"Bob", "Doyle", "Wayne", "Nao"};

  std::cout << sizeof(gpa) << " bytes\n"; // size of double is 8 bytes
  std::cout << sizeof(grade) << " bytes\n"; // size of char is 1 byte
  std::cout << sizeof(isStudent) << " bytes\n"; // size of boolean is 1 byte
  std::cout << sizeof(nums) << " bytes\n"; // size of the whole array

  std::cout << sizeof(name) << " bytes\n"; // size of strings the same whatever the string length is

  std::cout << sizeof(nums) / sizeof(int) << " bytes\n"; // calculate total element of array
  std::cout << sizeof(nums) / sizeof(nums[0]) << " numbers\n"; // another way to calculate total element of array
  std::cout << sizeof(students) / sizeof(students[0]) << " students\n"; // another way to calculate total element of array

  return 0;
}