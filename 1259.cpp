#include <iostream>
#include <vector>
using namespace std;


void print_it(int n) {
    vector<int> ns(5);
    int length = 0;
    for (int i = 0; i < 5; i++) {
        if (n != 0) {
            length++;
        }
        ns[i] = n % 10;
        n /= 10;
    }

    for (int i = 0; i < length / 2; i++) {
        if (ns[i] != ns[length - 1 - i]) {
            cout << "no" << "\n";
            return;
        }
    }
    cout << "yes" << "\n";
    return;
}


/**
 * 1259     팰린드롬수
 */
int main() {

    while (true) {
        int n;
        cin >> n;
        if (n == 0) {
            return 0;
        }

        print_it(n);
    }

}
