#include <iostream>

class Human {
  public:
    std::string name = "John Doe";
    std::string occupation = "Unknown";
    int age = 20;

    // overloading constructors
    Human(std::string name) {
      this->name = name;
    }

    Human(std::string name, int age) {
      this->name = name;
      this->age = age;
    }

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
   * 
   * overloaded constructors: multiple constructors with same name but different parameters allows for varying arguments when instatiating an object
   */

  Human human1 = Human("Rick", "Scientist", 60);
  Human human2 = Human("Micah", 50);

  std::cout << human1.name << "\n";
  std::cout << human1.occupation << "\n";
  std::cout << human1.age << "\n";

  human1.eat();
  human1.drink();
  human1.sleep();

  std::cout << human2.name << "\n";
  std::cout << human2.occupation << "\n";
  std::cout << human2.age << "\n";

  human2.eat();
  human2.drink();
  human2.sleep();

  return 0;
}