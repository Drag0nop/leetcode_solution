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

// Time Complexity: O(m*n)
// Space Complexity: O(m*n) for dp array + O(m+n) for recursion stack
int memorizationUniquePaths(int m, int n, int i, int j, vector<vector<int>>& dp) {
    if(i == m - 1 && j == n - 1) {
        return 1;
    }
    if(i >= m || j >= n) {
        return 0;
    }
    if(dp[i][j] != -1) {
        return dp[i][j];
    }
    int left = memorizationUniquePaths(m, n, i + 1, j, dp);
    int right = memorizationUniquePaths(m, n, i, j + 1, dp);
    return dp[i][j] = left + right;
}

// Time Complexity: O(m*n)
// Space Complexity: O(m*n) for dp array
int tabulationUniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 0));
    dp[0][0] = 1;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(i == 0 && j == 0) continue;
            int left = (i > 0) ? dp[i - 1][j] : 0;
            int right = (j > 0) ? dp[i][j - 1] : 0;
            dp[i][j] = left + right;
        }
    }
    return dp[m - 1][n - 1];
}

// Time Complexity: O(m*n)
// Space Complexity: O(n) for dp array
int optimizedTabulationUniquePaths(int m, int n) {
    vector<int> dp(n, 0);
    dp[0] = 1;
    for(int i = 0; i < m; i++) {
        vector<int> temp(n, 0);
        for(int j = 0; j < n; j++) {
            if(i == 0 && j == 0) {
                temp[j] = 1;
            } else {
                int left = (i > 0) ? dp[j] : 0;
                int right = (j > 0) ? temp[j - 1] : 0;
                temp[j] = left + right;
            }
        }
        dp = temp;
    }
    return dp[n - 1];
}
int main() {
    int m, n;
    cin >> m >> n;
    cout << recursionUniquePaths(m, n, 0, 0) << endl;
    vector<vector<int>> dp(m, vector<int>(n, -1));
    cout << memorizationUniquePaths(m, n, 0, 0, dp) << endl;
    cout << tabulationUniquePaths(m, n) << endl;
    cout << optimizedTabulationUniquePaths(m, n) << endl;
    return 0;
}