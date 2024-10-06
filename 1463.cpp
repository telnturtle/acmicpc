#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

int table[1000000 + 1];
const int MAX = 1000000 + 1;

/**
 * 1463         1로 만들기
 * 
 * @see https://www.acmicpc.net/problem/1463
 * 
 * dynamic programming solution
 */
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x;
    cin >> x;

    auto i = 0;

    while (i++ < x) {
        if (i == 1) {
            table[i] = 0;
        } else if (i == 2) {
            table[i] = 1;
        } else if (i == 3) {
            table[i] = 1;
        } else {
            vector<int> values = {table[i - 1] + 1, MAX, MAX};
            if (i % 2 == 0) {
                values[1] = table[i / 2] + 1;
            }
            if (i % 3 == 0) {
                values[2] = table[i / 3] + 1;
            }
            table[i] = *min_element(values.begin(), values.end());
        }
    }

    cout << table[x] << '\n';
}
