#include <iostream>

int main() {
  std::string name;
  std::string first, last, full;

  std::cout << "Enter your full name: ";
  // input full string with whitespace
  std::getline(std::cin >> std::ws, name);

  std::cout << "Enter your partner's first name: ";
  std::cin >> first;

  std::cout << "Enter your partner's last name: ";
  std::cin >> last;

  // append first and last name
  full = first;
  full.append(" ");
  full.append(last);

  // check if name is empty
  if (name.empty() || first.empty() || last.empty())
    std::cout << "Name is required.\n";
  // get name length
  else if (name.length() > 12 || full.length() > 12)
    std::cout << "Your name can't be over 12 chars.\n";
  else {
    std::string email = name.erase(0, name.find(' ') + 1);
    email.insert(email.length(), "@gmail.com");

    std::cout << "Your initial: " << name.at(0) << "\n";
    std::cout << "Your email: " << email << "\n";
    std::cout << "Welcome, monsieur " << name << "!\n\n";

    std::string f_email = last.append("@gmail.com");

    std::cout << "Your initial: " << full.at(0) << "\n";
    std::cout << "Your email: " << f_email << "\n";
    std::cout << "Also madame " << full << ".\n";
  }

  // remove name's value
  name.clear();

  std::cout << name << "\n";

  return 0;
}