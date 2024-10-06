#include <iostream>
using namespace std;


int table[1001];

int test(int a) {
    if (a == 1) {
        return 0;
    }
    int i = 2;

    while (i < a) {
        if (a % i == 0) {
            return 0;
        }
        i++;
    }
    return 1;
}

int main() {

    // initialize the table

    for (int i = 0; i < 1001; i++) {
        table[i] = test(i);
    }

    int n;
    cin >> n;

    int count = 0;

    while (n--) {
        int number;
        cin >> number;

        if (table[number] == 1) {
            count++;
        }
    }

    cout << count << endl;

    return 0;

}

