#include<bits/stdc++.h>
using namespace std;

int recursionTriangle(int i, int j, vector<vector<int>>& arr, int n) {
    if (i == n - 1) {
        return arr[n - 1][j];
    }
    int down = arr[i][j] + recursionTriangle(i + 1, j, arr, n);
    int diagonal = arr[i][j] + recursionTriangle(i + 1, j + 1, arr, n);
    return min(down, diagonal);
}

int memorizationTriangle(int i, int j, vector<vector<int>>& arr, int n, vector<vector<int>>& dp) {
    if (i == n - 1) {
        return arr[n - 1][j];
    }
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    int down = arr[i][j] + memorizationTriangle(i + 1, j, arr, n, dp);
    int diagonal = arr[i][j] + memorizationTriangle(i + 1, j + 1, arr, n, dp);
    return dp[i][j] = min(down, diagonal);
}

int tabulationTriangle(vector<vector<int>>& arr, int n) {
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int j = 0; j < n; j++) {
        dp[n - 1][j] = arr[n - 1][j];
    }
    for (int i = n - 2; i >= 0; i--) {
        for (int j = i; j >= 0; j--) {
            int down = arr[i][j] + dp[i + 1][j];
            int diagonal = arr[i][j] + dp[i + 1][j + 1];
            dp[i][j] = min(down, diagonal);
        }
    }
    return dp[0][0];
}

int optimizedTriangle(vector<vector<int>>& arr, int n) {
    vector<int> front(n, 0), curr(n, 0);
    for (int j = 0; j < n; j++) {
        front[j] = arr[n - 1][j];
    }
    for (int i = n - 2; i >= 0; i--) {
        for (int j = i; j >= 0; j--) {
            int down = arr[i][j] + front[j];
            int diagonal = arr[i][j] + front[j + 1];
            curr[j] = min(down, diagonal);
        }
        front = curr;
    }
    return front[0];
}
int main() {
    int n;
    cin >> n;
    vector<vector<int>> arr(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    cout << recursionTriangle(0, 0, arr, n) << endl;
    vector<vector<int>> dp(n, vector<int>(n, -1));
    cout << memorizationTriangle(0, 0, arr, n, dp) << endl;
    cout << tabulationTriangle(arr, n) << endl;
    cout << optimizedTriangle(arr, n) << endl;
    return 0;
}