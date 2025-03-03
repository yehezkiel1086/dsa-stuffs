#include <iostream>

int main() {
  /**
   * 1 types of type conversion:
   * - implicit / automatic
   * - explicit / manual
   */
  double x = (int) 3.14; // explicit

  std::cout << "x: " << x << "\n";

  int corr = 8;
  int quests = 10;
  double score = corr / (double) quests * 100;

  std::cout << "Score: " << score << "\n";

  return 0;
}