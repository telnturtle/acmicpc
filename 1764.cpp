#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * 1764        듣보잡
 */
int main() {
    int n, m;
    cin >> n >> m;

    set<string> nohear;
    string temp;
    vector<string> result;

    for (auto i = 0; i < n; i++) {
        cin >> temp;
        nohear.insert(temp);
    }
    for (auto i = 0; i < m; i++) {
        cin >> temp;
        if (nohear.count(temp)) {
            result.push_back(temp);
        }
    }

    sort(result.begin(), result.end());

    cout << result.size() << "\n";
    for (auto i = 0; i < result.size(); i++) {
        cout << result[i] << "\n";
    }

    return 0;
}
