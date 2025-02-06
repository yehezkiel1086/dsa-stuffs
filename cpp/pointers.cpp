#include <iostream>

// outputs memory addresses
void printMemories() {
  int a = 3, b = 2, c = 1; // 4 bytes difference each in memory
  std::cout << "Addresses: " << &a << " " << &b << " " << &c << "\n"; // returns memory addresses
}

// pointer address assignment from normal var
int *assignAddressFromVar(int var1) { // returns pointer
  int *p; // pointer declaration
  p = &var1; // address assignment

  // checking the address and value or var1
  std::cout << "Address of var1: " << &var1 << "\nValue of var1: " << var1 << "\n";
  return p;
}

// pointer address assignment from pointer var
int *assignAddressFromPointer(int *var3) {
  int *var4;
  *var4 = *var3; // pointer value assignment
  return var4;
}

// pointer value assignment
void setPointerVal(int *p, int val) {
  *p = val; // value assignment
}

int main() {
  printMemories();
  std::cout << std::endl;

  int *var2 = assignAddressFromVar(12);
  // checking the address and value of var2
  std::cout << "Address of var2: " << var2 << "\nValue of var2: " << *var2 << "\n\n"; // outputs address then value of pointer (dereference operator: *)

  int *var3;
  setPointerVal(var3, 13);
  std::cout << "Value of var3: " << *var3 << "\nAddress of var3: " << var3 << "\n";
  int *var4 = assignAddressFromPointer(var3);
  std::cout << "Value of var4: " << *var4 << "\nAddress of var4: " << var4 << "\n\n";
  return 0;
}