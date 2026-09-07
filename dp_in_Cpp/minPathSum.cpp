#include<bits/stdc++.h>
using namespace std;

int recursionMinPathSum(int m, int n, vector<vector<int>>& arr) {
    if (m == 0 && n == 0) {
        return arr[m][n];
    }
    if (m < 0 || n < 0) {
        return INT_MAX;
    }
    int up = arr[m][n] + recursionMinPathSum(m - 1, n, arr);
    int left = arr[m][n] + recursionMinPathSum(m, n - 1, arr);
    return min(up, left);
}

int memorizationMinPathSum(int m, int n, vector<vector<int>>& arr, vector<vector<int>>& dp) {
    if (m == 0 && n == 0) {
        return arr[m][n];
    }
    if (m < 0 || n < 0) {
        return INT_MAX;
    }
    if (dp[m][n] != -1) {
        return dp[m][n];
    }
    int up = arr[m][n] + memorizationMinPathSum(m - 1, n, arr, dp);
    int left = arr[m][n] + memorizationMinPathSum(m, n - 1, arr, dp);
    return dp[m][n] = min(up, left);
}

int tabulationMinPathSum(int m, int n, vector<vector<int>>& arr) {
    vector<vector<int>> dp(m, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) {
                dp[i][j] = arr[i][j];
            }
            else {
                int up = arr[i][j];
                if (i > 0) {
                    up += dp[i - 1][j];
                }
                else {
                    up += INT_MAX;
                }
                int left = arr[i][j];
                if (j > 0) {
                    left += dp[i][j - 1];
                }
                else {
                    left += INT_MAX;
                }
                dp[i][j] = min(up, left);
            }
        }
    }
    return dp[m - 1][n - 1];
}


int optimizationMinPathSum(int m, int n, vector<vector<int>>& arr) {
    vector<int> prev(n, 0);
    for (int i = 0; i < m; i++) {
        vector<int> curr(n, 0);
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) {
                curr[j] = arr[i][j];
            }
            else {
                int up = arr[i][j];
                if (i > 0) {
                    up += prev[j];
                }
                else {
                    up += INT_MAX;
                }
                int left = arr[i][j];
                if (j > 0) {
                    left += curr[j - 1];
                }
                else {
                    left += INT_MAX;
                }
                curr[j] = min(up, left);
            }
        }
        prev = curr;
    }
    return prev[n - 1];
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
    cout << recursionMinPathSum(m - 1, n - 1, arr) << endl;
    vector<vector<int>> dp(m, vector<int>(n, -1));
    cout << memorizationMinPathSum(m - 1, n - 1, arr, dp) << endl;
    cout << tabulationMinPathSum(m, n, arr) << endl;
    cout << optimizationMinPathSum(m, n, arr) << endl;
    return 0;
}