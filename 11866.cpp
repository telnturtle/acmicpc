#include <iostream>
#include <vector>
// #include <iomanip>
using namespace std;


/**
 * 11866        요세푸스 문제 0
 */
int main() {
    int n, k;
    cin >> n >> k;

    // initialize the table

    vector<bool> table(n);
    for (auto i = 0; i < n; i++) {
        table[i] = true;
    }

    int i = 0;
    int step = 0;
    vector<int> result(n);
    int length = 0;

    while (true) {
        // cout << "i: " << i << " j: " << i + 1 << " step: " << step << " length: " << length << " table: " << table[0] << table[1] << table[2] << table[3] << table[4] << table[5] << table[6] << " result: " << result[0] << result[1] << result[2] << result[3] << result[4] << result[5] << result[6] << "\n";
        step++;
        if (step == k) {
            step = 0;
            table[i] = false;

            int j = i + 1;
            result[length] = j;
            length++;
        }

        if (length == n) {
            break;
        }

        while (true) {
            i = (i + 1) % n;
            if (table[i]) {
                break;
            }
        }
    }

    cout << "<";
    for (auto i = 0; i < n; i++) {
        cout << result[i];
        if (i != n - 1) {
            cout << ", ";
        }
    }
    cout << ">" << "\n";

    return 0;
}
