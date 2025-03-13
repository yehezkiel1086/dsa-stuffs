#include <iostream>

struct student {
  std::string name;
  double gpa;
  bool enrolled = false;
};

struct Car {
  std::string model;
  int year;
  std::string color;
};

void printCar(Car &car);
void paintCar(Car &car, std::string color);

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

  Car car1;
  Car car2;

  car1.model = "Toyota Supra MK4";
  car1.color = "White";
  car1.year = 2001;

  paintCar(car1, "Black");

  std::cout << &car1 << "\n";
  printCar(car1);

  car2.model = "Nissan GTR R34";
  car2.color = "White";
  car2.year = 2000;

  paintCar(car2, "Gold");

  std::cout << &car2 << "\n";
  printCar(car2);

  return 0;
}

void paintCar(Car &car, std::string color) {
  car.color = color;
}

void printCar(Car &car) {
  std::cout << &car << "\n";
  std::cout << car.model << "\n";
  std::cout << car.year << "\n";
  std::cout << car.color << "\n";
}