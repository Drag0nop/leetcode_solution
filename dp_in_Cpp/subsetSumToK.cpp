#include<bits/stdc++.h>
using namespace std;

bool recursive(int ind, int target, vector<int>& arr) {
    if (target == 0) return true;
    if (ind == 0) return arr[0] == target;
    bool notTake = recursive(ind - 1, target, arr);
    bool take = false;
    if (arr[ind] <= target) {
        take = recursive(ind - 1, target - arr[ind], arr);
    }
    return take | notTake;
}

bool memorization(int ind, int target, vector<int>& arr, vector<vector<int>>& dp) {
    if (target == 0) return true;
    if (ind == 0) return arr[0] == target;
    if (dp[ind][target] != -1)
        return dp[ind][target];
    bool notTake = memorization(ind - 1, target, arr, dp);
    bool take = false;
    if (arr[ind] <= target)
        take = memorization(ind - 1, target - arr[ind], arr, dp);
    return dp[ind][target] = take | notTake;
}

bool tabulation(int n, int target, vector<int>& arr) {
    vector<vector<bool>> dp(n, vector<bool>(target + 1, 0));
    for (int i = 0; i < n; i++) {
        dp[i][0] = true;
    }
    dp[0][arr[0]] = true;
    for (int ind = 1; ind < n; ind++) {
        for (int t = 1; t <= target; t++) {
            bool notTake = dp[ind - 1][t];
            bool take = false;
            if (arr[ind] <= t) {
                take = dp[ind - 1][t - arr[ind]];
            }
            dp[ind][t] = take | notTake;
        }
    }
    return dp[n - 1][target];
}

bool optimized(int n, int target, vector<int>& arr) {
    vector<bool> prev(target + 1, 0), curr(target + 1, 0);
    prev[0] = curr[0] = true;
    prev[arr[0]] = true;
    for (int ind = 1; ind < n; ind++) {
        for (int t = 1; t <= target; t++) {
            bool notTake = prev[t];
            bool take = false;
            if (arr[ind] <= t) {
                take = prev[t - arr[ind]];
            }
            curr[t] = take | notTake;
        }
        prev = curr;
    }
    return prev[target];
}
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    if (recursive(n - 1, k, arr)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    vector<vector<int>> dp(n, vector<int>(k + 1, -1));
    if (memorization(n - 1, k, arr, dp)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    if (tabulation(n, k, arr)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}