#include <iostream>
#include <cmath>

int main() {
  double x = 3, y = 4, z;

  z = std::max(x, y);
  z = std::min(x, y);
  z = pow(2, 4);
  z = sqrt(16);
  z = abs(-3);
  z = ceil(3.14);
  z = floor(3.14);
  z = round(3.14);

  std::cout << z << std::endl;

  return 0;
}