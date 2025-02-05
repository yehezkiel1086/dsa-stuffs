#include <iostream>
#include <math.h>

// returns the sum of the first n natural numbers
int recursiveSum(int n) {
  // stop recursion when n is 1
  if (n == 1) {
    return 1;
  }

  return n + recursiveSum(n - 1);
}

// returns the sum of the first n even numbers squares
int squares(int n) {
  if(n == 1) {
    return 1;
  }

  return pow(n, 2) + squares(n - 1);
}

// returns the sum of the first n even numbers squares
int evenSquares(int n) {
  // stop recursion when n is 1
  if(n == 1) {
    return 0;
    // check if n is even
  } else if(n % 2 == 0) {
    // sum of even numbers squares
    return pow(n, 2) + evenSquares(n - 1);
  }

  // if number is off - do nothing and call function again
  return evenSquares(n - 1);
}

// return the nth fibonacci number
int fibNum(int n) {
  // stop recursion when n is 0 or 1
  if(n <= 1)
    return n;
  return fibNum(n - 1) + fibNum(n - 2);
}

// return true if string s with length l contains char c -- otherwise false
bool linear(std::string s, char c, int l) {
  // do linear search from back to front
  if(l < 0)
    return false;
  // if string index == char
  else if(s[l] == c)
    return true;
  // repeat linear search and decrement index
  return linear(s, c, l - 1);
}

int main() {
  int sum = recursiveSum(5);
  int evenSum = evenSquares(5);
  bool contH = linear("cicago", 'h', 7);

  std::cout << "Sum of the first 5 natural numbers: " << sum << std::endl;

  std::cout << "Sum of the first 5 even numbers squares: " << evenSum << std::endl;

  std::cout << "Contains H: " << contH << std::endl;

  return 0;
}