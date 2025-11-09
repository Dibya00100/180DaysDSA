// Problem: Reverse a Number
// Difficulty: Easy


#include <iostream>
#include <climits>
using namespace std;

long long reverse_number(long long n) {
    long long sign = n < 0 ? -1 : 1;
    n = llabs(n);
    
    long long rev = 0;
    while (n) {
        rev = rev * 10 + (n % 10);
        n /= 10;

        // Overflow detection before multiplying or adding
        if (rev > (LLONG_MAX - n % 10) / 10) {
            cerr << "Overflow detected!\n";
            return 0;
        }
    }
    return sign * rev;
}

int main() {
    cout << reverse_number(1234) << "\n";
    return 0;
}
