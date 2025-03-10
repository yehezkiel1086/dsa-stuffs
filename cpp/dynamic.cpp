#include <iostream>

int main() {
  /**
   * dynamic memory = memory that's allocated after the program is already compiled and running.
   * - Use 'new' operator to allocate memory in the heap rather than the stack.
   * - Useful when we don't know how much memory needed.
   * - Makes our program more flexible, especially when accepting user input.
   */

  
  char *pGrades = NULL;
  int gSize;

  std::cout << "Enter total grades: ";
  std::cin >> gSize;
  
  pGrades = new char[gSize];

  for(int i = 0; i < gSize; i++) {
    std::cout << "Enter grade #" << i << ": ";
    std::cin >> pGrades[i];
  }

  std::cout << "Grades you entered: ";
  for(int i = 0; i < gSize; i++) {
    std::cout << pGrades[i] << " ";
  }
  std::cout << "\n";

  delete []pGrades;

  int *pNum = NULL;
  pNum = new int;
  *pNum = 21;

  std::cout << "address: " << pNum << "\nvalue: " << *pNum << "\n";

  delete pNum; // freeing up the memory (no memory leaks)

  return 0;
}