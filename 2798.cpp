#include <iostream>
#include <vector>
using namespace std;


/**
 * O(n**3) solution
 */
int main() {
    int n, m;
    cin >> n >> m;

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int sum_max = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (i != j && j != k && i != k) {
                    int sum = arr[i] + arr[j] + arr[k];
                    if (sum <= m && sum > sum_max) {
                        sum_max = sum;
                    }
                }
            }
        }
    }

    cout << sum_max << "\n";

    return 0;
}
