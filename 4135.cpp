#include <iostream>
using namespace std;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    while (true) {
        int x, y, z;
        cin >> x >> y >> z;
        if (x == 0 && y == 0 && z == 0) {
            return 0;
        }

        if (x > y) {
            swap(&x, &y);
        }
        if (y > z) {
            swap(&y, &z);
        }

        // x < z and y < z

        if (z * z == x * x + y * y) {
            cout << "right" << endl;
        } else {
            cout << "wrong" << endl;
        }

    }
}

