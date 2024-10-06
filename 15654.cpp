#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
array<int, 8> ns = { 10'001, };

void f(unordered_set<int> s, vector<int> v) {

    if (s.size() == m) {
        for (auto i = 0; i < m - 1; i++) {
            cout << v[i] << ' ';
        }
        cout << v[m - 1] << '\n';
        return;
    }

    for (auto i = 0; i < n; i++) {
        if (s.count(ns[i]) > 0) {
            continue;
        }
        unordered_set<int> s1(s);
        s1.insert(ns[i]);
        vector<int> v1(v);
        v1.push_back(ns[i]);
        f(s1, v1);
    }

}


/**
 * 15654        N과 M (5)
 * 
 * @see https://www.acmicpc.net/problem/15654
 * 
 * recursive solution
 */
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for (auto i = 0; i < n; i++) {
        cin >> ns[i];
    }
    for (auto i = n; i < 8; i++) {
        ns[i] = 10'001;
    }

    sort(ns.begin(), ns.end());

    f(unordered_set<int>(), vector<int>());

    return 0;

}
