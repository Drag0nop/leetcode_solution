#include<bits/stdc++.h>
using namespace std;

int recursionMaxPath(int i, int j, vector<vector<int>>& arr) {
    if (i == 0) {
        return arr[0][j];
    }
    if (j < 0 || j >= arr[0].size()) {
        return INT_MIN;
    }
    int s = arr[i][j] + recursionMaxPath(i - 1, j, arr);
    int ld = arr[i][j] + recursionMaxPath(i - 1, j - 1, arr);
    int rd = arr[i][j] + recursionMaxPath(i - 1, j + 1, arr);
    return max(s, max(ld, rd));
}

int memorizationMaxPath(int i, int j, vector<vector<int>>& arr, vector<vector<int>>& dp) {
    if (i == 0) {
        return arr[0][j];
    }
    if (j < 0 || j >= arr[0].size()) {
        return INT_MIN;
    }
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    int s = arr[i][j] + memorizationMaxPath(i - 1, j, arr, dp);
    int ld = arr[i][j] + memorizationMaxPath(i - 1, j - 1, arr, dp);
    int rd = arr[i][j] + memorizationMaxPath(i - 1, j + 1, arr, dp);
    dp[i][j] = max(s, max(ld, rd));
    return dp[i][j];
}

int tabulationMaxPath(vector<vector<int>>& arr, int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 0));
    for (int j = 0; j < n; j++) {
        dp[0][j] = arr[0][j];
    }
    for (int i = 1; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int s = arr[i][j] + dp[i - 1][j];
            int ld = arr[i][j];
            if (j - 1 >= 0) {
                ld += dp[i - 1][j - 1];
            }
            else {
                ld += INT_MIN;
            }
            int rd = arr[i][j];
            if (j + 1 < n) {
                rd = rd + dp[i - 1][j + 1];
            }
            else {
                rd += INT_MIN;
            }
            dp[i][j] = max(s, max(ld, rd));
        }
    }
    int res = INT_MIN;
    for (int j = 0; j < n; j++) {
        res = max(res, dp[m - 1][j]);
    }
    return res;
}

int optimizationMaxPath(vector<vector<int>>& arr, int m, int n) {
    vector<int> prev(n, 0);
    for (int j = 0; j < n; j++) {
        prev[j] = arr[0][j];
    }
    for (int i = 1; i < m; i++) {
        vector<int> curr(n, 0);
        for (int j = 0; j < n; j++) {
            int s = arr[i][j] + prev[j];
            int ld = arr[i][j];
            if (j - 1 >= 0) {
                ld += prev[j - 1];
            }
            else {
                ld += INT_MIN;
            }
            int rd = arr[i][j];
            if (j + 1 < n) {
                rd = rd + prev[j + 1];
            }
            else {
                rd += INT_MIN;
            }
            curr[j] = max(s, max(ld, rd));
        }
        prev = curr;
    }
    int res = INT_MIN;
    for (int j = 0; j < n; j++) {
        res = max(res, prev[j]);
    }
    return res;
}
int main() {
    int n, m;
    cin >> m >> n;
    vector<vector<int>> arr(m, vector<int>(n));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    cout << recursionMaxPath(m - 1, n - 1, arr) << endl;
    vector<vector<int>> dp(m, vector<int>(n, -1));
    cout << memorizationMaxPath(m - 1, n - 1, arr, dp) << endl;
    cout << tabulationMaxPath(arr, m, n) << endl;
    cout << optimizationMaxPath(arr, m, n) << endl;
    return 0;
}