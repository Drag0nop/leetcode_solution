#include<bits/stdc++.h>
using namespace std;

// Time Complexity: O(2^(m+n))
// Space Complexity: O(m+n) for recursion stack
int recursionUniquePaths(int m, int n) {
    if(m == 1 && n == 1) {
        return 1;
    }
    if(m <= 0 || n <= 0) {
        return 0;
    }
    int left = recursionUniquePaths(m - 1, n);
    int right = recursionUniquePaths(m, n - 1);
    return left + right;
}

// Time Complexity: O(m*n)
// Space Complexity: O(m*n) for dp array + O(m+n) for recursion stack
int memorizationUniquePaths(int m, int n, vector<vector<int>>& dp) {
    if(m == 1 && n == 1) {
        return 1;
    }
    if(m <= 0 || n <= 0) {
        return 0;
    }
    if(dp[m - 1][n - 1] != -1) {
        return dp[m - 1][n - 1];
    }
    int left = memorizationUniquePaths(m - 1, n, dp);
    int right = memorizationUniquePaths(m, n - 1, dp);
    return dp[m - 1][n - 1] = left + right;
}

// Time Complexity: O(m*n)
// Space Complexity: O(m*n) for dp array
int tabulationUniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 0));
    dp[0][0] = 1;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(i == 0 && j == 0) continue;
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
                int left = 0, right = 0;
                if (i > 0) {
                    left = dp[j];
                }
                if (j > 0) {
                    right = temp[j - 1];
                }
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
    cout << recursionUniquePaths(m, n) << endl;
    vector<vector<int>> dp(m, vector<int>(n, -1));
    cout << memorizationUniquePaths(m, n, dp) << endl;
    cout << tabulationUniquePaths(m, n) << endl;
    cout << optimizedTabulationUniquePaths(m, n) << endl;
    return 0;
}