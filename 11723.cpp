#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>

using namespace std;

const string add        = "add"    ;
const string remove0    = "remove" ;
const string check      = "check"  ;
const string toggle     = "toggle" ;
const string all        = "all"    ;
const string empty0     = "empty"  ;

/**
 * 11723        집합
 * 
 * @see https://www.acmicpc.net/problem/11723
 * 
 * bitmask solution
 */
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m = 0;
    cin >> m;
    string command;
    int i = 0;
    int index = 1000;

    int table = 0;

    while (i++ < m) {
        cin >> command;
        if (command == add) {
            cin >> n;
            table |= 1 << n;
        } else if (command == remove0) {
            cin >> n;
            table &= 0 << n;
        } else if (command == check) {
            cin >> n;
            cout << (int) ((bool) (table & (1 << n))) << '\n';
        } else if (command == toggle) {
            cin >> n;
            table ^= 1 << n;
        } else if (command == all) {
            table = (1 << 21) - 1;
        } else if (command == empty0) {
            table = 0;
        }
    }

    return 0;
}
