#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;

void f(int base, vector<int> v) {

    if (v.size() == m) {
        for (auto i = 0; i < m - 1; i++) {
            cout << v[i] << ' ';
        }
        cout << v[m - 1] << '\n';
        return;
    }

    for (int i = base; i <= n; i++) {
        vector<int> v1(v);
        v1.push_back(i);
        f(i, v1);
    }

}


/**
 * 15652        N과 M (4)
 * 
 * @see https://www.acmicpc.net/problem/15652
 * 
 * recursive solution
 */
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        f(i, vector<int>(1, i));
    }

    return 0;

}
