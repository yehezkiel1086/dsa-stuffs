#include <iostream>
#include <vector>

typedef std::vector<std::pair<std::string, int>> pairlist_t;

typedef std::string name_t;
typedef int age_t;

// `using` is the same with `typedef`
using address_t = std::string;
using height_t = float;

int main() {
  /**
   * typedef:
   * - Reserved keyword to create additional name (alias) for another data type.
   * - New identifier for existing data type
   * - Helps with readability and reduces typos
   * - Use when there's clear benefit (`using` works better w/ templates)
   */
  
  pairlist_t pairlist;

  name_t name = "Benjamin";
  age_t age = 21;
  address_t addr = "Park Avenue st.";
  height_t height = 175.6;

  std::cout << "Name: " << name << "\n";
  std::cout << "Age: " << age << "\n";
  std::cout << "Address: " << addr << "\n";
  std::cout << "Height: " << height << " cm\n";

  return 0;
}