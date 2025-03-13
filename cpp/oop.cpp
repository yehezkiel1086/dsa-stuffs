#include <iostream>

class Human {
  public:
    std::string name = "John Doe";
    std::string occupation = "Unknown";
    int age = 20;

    Human(std::string name, std::string occupation, int age) {
      this->name = name;
      this->occupation = occupation;
      this->age = age;
    }

    void eat() {
      std::cout << "This person is eating" << "\n";
    }

    void drink() {
      std::cout << "This person is drinking" << "\n";
    }

    void sleep() {
      std::cout << "This person is sleeping" << "\n";
    }
};

int main() {
  /**
   * object: a collection of attributes and methods.
   * - can have characteristics and could perform actions
   * - can be used to mimic real world items (e.g: phone, book, etc)
   * - created from a class which acts as "blue-print"
   * 
   * constructor: a special method that's automatically called when an object is instantiated, useful for assigning values to attributes as arguments
   */

  Human human1 = Human("Rick", "Scientist", 60);

  std::cout << human1.name << "\n";
  std::cout << human1.occupation << "\n";
  std::cout << human1.age << "\n";

  human1.eat();
  human1.drink();
  human1.sleep();

  return 0;
}