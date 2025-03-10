#include <iostream>
#include <vector>

using std::string;
using std::cout;
using age_t = int;
using name_t = string;

typedef std::vector<std::pair<int, string>> pairlst_t;

namespace first {
  int x = 1;
}

namespace second {
  int x = 2;
}

namespace fName {
  string name = "Benzion";
}

namespace lName {
  string name = "Yehezkel";
}

int main() {
  using namespace second;
  using namespace fName;

  pairlst_t pairlst;

  cout << "First name: " << name << "\n";
  cout << "Second: " << x << "\n";

  return 0;
}