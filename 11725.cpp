#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

const int MAX = 100'001;


/**
 * 11725        트리의 부모 찾기
 * 
 * @see https://www.acmicpc.net/problem/11725
 * 
 * breadth first search solution
 */
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unsigned int n;
    cin >> n;

    vector<int> tree[MAX];
    vector<int> parents(MAX);
    unordered_set<int> visited;

    for (auto i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        tree[x].push_back(y);
        tree[y].push_back(x);
    }

    // do bfs

    queue<int> q;
    q.push(1);

    int node;

    while (q.front()) {
        node = q.front();
        q.pop();
        visited.insert(node);

        for (auto i : tree[node]) {
            if (!visited.count(i)) {
                parents[i] = node;
                q.push(i);
            }
        }
    }

    for (auto i = 2; i <= n; i++) {
        cout << parents[i] << '\n';
    }

    return 0;

}
