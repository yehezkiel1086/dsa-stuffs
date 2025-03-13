#include <iostream>

class Human {
  private:
    std::string name = "John Doe";
    std::string occupation = "Unknown";
    int age = 20;
  public:
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

    // setters
    void setName(std::string name) {
      // could do more logics here
      this->name = name;
    }

    void setOccupation(std::string occupation) {
      // could do more logics here
      this->occupation = occupation;
    }

    void setAge(int age) {
      // could do more logics here
      this->age = age;
    }

    // getters
    std::string getName() {
      return this->name;
    }

    std::string getOccupation() {
      return this->occupation;
    }

    int getAge() {
      return this->age;
    }

    // methods
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

// inheritance
class Shape {
  public:
    double area;
    double circ;

    void setArea(double area) {
      this->area = area;
    }

    void setCirc(double circ) {
      this->circ = circ;
    }

    double getArea() {
      return this->area;
    }

    double getCirc() {
      return this->circ;
    }
};

class Square: public Shape {
  private:
    double side;
  public:
    void setArea() {
      this->area = this->side * this->side;
    }

    void setCirc() {
      this->circ = 4 * this->side;
    }

    Square(double side) {
      this->side = side;
      this->setArea();
      this->setCirc();
    }
};

class Triangle: public Shape {
  private:
    double height, bottom;
  public:
    Triangle(double height, double bottom) {
      this->height = height;
      this->bottom = bottom;
    }

    void setArea() {
      this->area = this->height * this->bottom * 0.5;
    }

    void setCirc() {
      this->circ = this->bottom * 3;
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
   * 
   * Abstraction: hiding unnecesssary data from outside a class
   * getter: function that makes a private attribute READABLE
   * setter: function that makes a private attribute WRITEABLE
   * 
   * inheritance: a class can receive attributes and methods from another class
   * - children classes inherit from a parent class
   * - helps to reuse similar code found within multiple classes
   */

  Human human1 = Human("Rick", "Scientist", 60);
  Human human2 = Human("Micah", 50);

  human2.setOccupation("Outlaw");

  std::cout << human1.getName() << "\n";
  std::cout << human1.getOccupation() << "\n";
  std::cout << human1.getAge() << "\n";

  human1.eat();
  human1.drink();
  human1.sleep();

  std::cout << human2.getName() << "\n";
  std::cout << human2.getOccupation() << "\n";
  std::cout << human2.getAge() << "\n";

  human2.eat();
  human2.drink();
  human2.sleep();

  Square s1 = Square(4);
  std::cout << "Area: " << s1.getArea() << "\n";
  std::cout << "Circumference: " << s1.getCirc() << "\n";

  return 0;
}