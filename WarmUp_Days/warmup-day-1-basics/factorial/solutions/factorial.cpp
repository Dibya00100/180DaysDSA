// Problem: Factorial of a Number
// Difficulty: Easy

#include <iostream>
using namespace std;

long long factorial(int n) {
    long long res = 1;
    for (int i = 2; i <= n; ++i) res *= i;
    return res;
}

int main() {
    cout << factorial(5) << "\n";
    return 0;
}
