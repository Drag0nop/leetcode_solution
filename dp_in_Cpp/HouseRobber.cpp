#include<bits/stdc++.h>
using namespace std;

int recursive(vector<int>& arr, int n) {
    if (n == 0) return arr[n];
    if (n < 0) return 0;
    int pick = arr[n] + recursive(arr, n - 2);
    int not_pick = 0 + recursive(arr, n - 1);
    return max(pick, not_pick);
}

int memorization(vector<int>& arr, int n, vector<int>& dp) {
    if (n == 0) return arr[n];
    if (n < 0) return 0;
    if (dp[n] != -1) return dp[n];
    int pick = arr[n] + memorization(arr, n - 2, dp);
    int not_pick = memorization(arr, n - 1, dp);
    return dp[n] = max(pick, not_pick);
}

int tabulation(vector<int>& arr, int n) {
    vector<int> dp(n);
    dp[0] = arr[0];
    for (int i = 1; i < n; i++) {
        int pick = arr[i];
        if (i > 1) pick += dp[i - 2];
        int not_pick = dp[i - 1];
        dp[i] = max(pick, not_pick);
    }
    return dp[n - 1];
}

int Optimize(vector<int>& arr, int n) {
    int prev2 = 0;
    int prev1 = arr[0];
    for (int i = 1; i < n; i++) {
        int pick = arr[i];
        if (i > 1) pick += prev2;
        int not_pick = prev1;
        int curr = max(pick, not_pick);
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> dp(n, -1);
    cout << "Recursive: " << recursive(arr, n - 1) << endl;
    cout << "Memorization: " << memorization(arr, n - 1, dp) << endl;
    cout << "Tabulation: " << tabulation(arr, n) << endl;
    cout << "Space Optimization: " << Optimize(arr, n) << endl;
    return 0;
}