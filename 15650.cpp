#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

int m, n;

void f(int base, vector<int> v) {
    // cout << "base: " << base << "\t\t v: ";
    // for (auto i : v) {
    //     cout << i << ' ';
    // }
    // cout << '\n';

    if (v.size() == m) {
        for (auto i = 0; i < m - 1; i++) {
            cout << v[i] << ' ';
        }
        cout << v[m - 1] << '\n';
        return;
    }

    for (auto i = base + 1; i <= n; i++) {
        vector<int> v1(v);
        v1.push_back(i);
        f(i, v1);
    }
}


/**
 * 15650        N과 M (2)
 * 
 * @see https://www.acmicpc.net/problem/15650
 * 
 * recursive solution
 */
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    f(0, vector<int>());

    return 0;

}
