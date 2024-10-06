#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;


/**
 * 1546     평균
 */
int main() {
    int n, m, sum;
    cin >> n;
    vector<int> scores(n);
    for (auto i = 0; i < n; i++) {
        cin >> scores[i];
    }

    m = 0;
    sum = 0;
    for (auto i = 0; i < n; i++) {
        int score = scores[i];
        sum += score;
        if (score > m) {
            m = score;
        }
    }

    // m is max score value

    cout << fixed << setprecision(3) << ((double) sum / n) * 100 / m << "\n";

    return 0;
}
