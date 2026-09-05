#include<bits/stdc++.h>
using namespace std;

// Time Complexity: O(2^(m+n))
// Space Complexity: O(m+n) for recursion stack
int recursionUniquePaths2(int m, int n, vector<vector<int>>& arr) {
    if (m == 1 && n == 1) {
        return 1;
    }
    if (m <= 0 || n <= 0 || arr[m - 1][n - 1] == 1) {
        return 0;
    }
    int left = recursionUniquePaths2(m - 1, n, arr);
    int right = recursionUniquePaths2(m, n - 1, arr);
    return left + right;
}

// Time Complexity: O(m*n)
// Space Complexity: O(m*n) for dp array + O(m+n) for recursion stack
int memorizationUniquePaths2(int m, int n, vector<vector<int>>& arr, vector<vector<int>>& dp) {
    if (m == 1 && n == 1) {
        return 1;
    }
    if (m <= 0 || n <= 0 || arr[m - 1][n - 1] == 1) {
        return 0;
    }
    if (dp[m - 1][n - 1] != -1) {
        return dp[m - 1][n - 1];
    }
    int left = memorizationUniquePaths2(m - 1, n, arr, dp);
    int right = memorizationUniquePaths2(m, n - 1, arr, dp);
    dp[m - 1][n - 1] = left + right;
    return dp[m - 1][n - 1];
}

// Time Complexity: O(m*n)
// Space Complexity: O(m*n) for dp array
int tabulationUniquePaths2(int m, int n, vector<vector<int>>& arr) {
    vector<vector<int>> dp(m, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][j] == 1) {
                dp[i][j] = 0;
            }
            else if (i == 0 && j == 0) {
                dp[i][j] = 1;
            }
            else {
                int left = 0, right = 0;
                if (i > 0) {
                    left = dp[i - 1][j];
                }
                if (j > 0) {
                    right = dp[i][j - 1];
                }
                dp[i][j] = left + right;
            }
        }
    }
    return dp[m - 1][n - 1];
}
int main() {
    int m, n;
    cin >> m >> n;
    vector<vector<int>> arr(m, vector<int>(n));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    cout << recursionUniquePaths2(m, n, arr) << endl;
    vector<vector<int>> dp(m, vector<int>(n, -1));
    cout << memorizationUniquePaths2(m, n, arr, dp) << endl;
    cout << tabulationUniquePaths2(m, n, arr) << endl;
    return 0;
}