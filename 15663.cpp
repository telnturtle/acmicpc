#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;


int n, m;
array<int, 9> ns = { 0, };
bool isVisited[9] = { false, };


void f(vector<int> v) {

    if (v.size() == m) {
        for (auto i = 0; i < m - 1; i++) {
            cout << v[i] << ' ';
        }
        cout << v[m - 1] << '\n';
        return;
    }

    int previous = 0;

    for (auto i = 1; i <= n; i++) {
        int number = ns.at(i);
        if (isVisited[i] || previous == number) {
            continue;
        }

        isVisited[i] = true;
        previous = number;

        vector<int> v1(v);
        v1.push_back(number);

        f(v1);
        isVisited[i] = false;
    }
}

/**
 * 15663        N과 M (9)
 * 
 * @see https://www.acmicpc.net/problem/15663
 * 
 * recursive solution
 */
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    for (auto i = 1; i <= n; i++) {
        cin >> ns[i];
    }

    sort(ns.begin(), ns.begin() + n + 1);

    f(vector<int>(0, 0));

    return 0;

}
