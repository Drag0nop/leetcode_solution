#include<bits/stdc++.h>
using namespace std;

// Time Complexity: O(2^(m+n))
// Space Complexity: O(m+n) for recursion stack
int recursionUniquePaths(int m, int n, int i, int j) {
    if(i == m - 1 && j == n - 1) {
        return 1;
    }
    if(i >= m || j >= n) {
        return 0;
    }
    int left = recursionUniquePaths(m, n, i + 1, j);
    int right = recursionUniquePaths(m, n, i, j + 1);
    return left + right;
}
int main() {
    int m, n;
    cin >> m >> n;
    cout << recursionUniquePaths(m, n, 0, 0) << endl;
    return 0;
}