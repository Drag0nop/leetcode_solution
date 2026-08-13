#include<bits/stdc++.h>
using namespace std;

int recursiveFrogJumpKthTimes(int n, const vector<int>& height, int k) {
    if (n == 0) return 0;
    int minCost = INT_MAX;
    for (int j = 1; j <= k; j++) {
        if (n - j >= 0) {
            int cost = recursiveFrogJumpKthTimes(n - j, height, k) + abs(height[n] - height[n - j]);
            minCost = min(minCost, cost);
        }
    }
    return minCost;
}

int memorizationFrogJumpKthTimes(int n, const vector<int>& height, int k, vector<int>& dp) {
    if (n == 0) return 0;
    if (dp[n] != -1) return dp[n];
    int minCost = INT_MAX;
    for (int j = 1; j <= k; j++) {
        if (n - j >= 0) {
            int cost = memorizationFrogJumpKthTimes(n - j, height, k, dp) + abs(height[n] - height[n - j]);
            minCost = min(minCost, cost);
        }
    }
    return dp[n] = minCost;
}

int tabulationFrogJumpKthTimes(int n, const vector<int>& height, int k) {
    vector<int> dp(n, 0);
    dp[0] = 0;
    for (int i = 1; i < n; i++) {
        int minCost = INT_MAX;
        for (int j = 1; j <= k; j++) {
            if (i - j >= 0) {
                int cost = dp[i - j] + abs(height[i] - height[i - j]);
                minCost = min(minCost, cost);
            }
        }
        dp[i] = minCost;
    }
    return dp[n - 1];
}

int optimizedFrogJumpKthTimes(int n, const vector<int>& height, int k) {
    vector<int> dp(k, 0);
    dp[0] = 0;
    for (int i = 1; i < n; i++) {
        int minCost = INT_MAX;
        for (int j = 1; j <= k; j++) {
            if (i - j >= 0) {
                int cost = dp[i - j] + abs(height[i] - height[i - j]);
                minCost = min(minCost, cost);
            }
        }
        dp[i % k] = minCost;
    }
    return dp[(n - 1) % k];
}

int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }
    int k;
    cin >> k;
    cout << "Minimum energy required: " << recursiveFrogJumpKthTimes(n - 1, height, k) << endl;
    vector<int> dp(n, -1);
    cout << "Minimum energy required: " << memorizationFrogJumpKthTimes(n - 1, height, k, dp) << endl;
    cout << "Minimum energy required: " << tabulationFrogJumpKthTimes(n, height, k) << endl;
    cout << "Minimum energy required: " << optimizedFrogJumpKthTimes(n, height, k) << endl;
    return 0;
}