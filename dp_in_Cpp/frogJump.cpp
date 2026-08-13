#include<bits/stdc++.h>
using namespace std;

int recursiveFrogJump(int n, const vector<int>& height) {
    if (n == 0) return 0;
    int left = recursiveFrogJump(n - 1, height) + abs(height[n] - height[n - 1]);
    int right = INT_MAX;
    if (n > 1) {
        right = recursiveFrogJump(n - 2, height) + abs(height[n] - height[n - 2]);
    }
    return min(left, right);
}

int dpFrogJump(int n, const vector<int>& height, vector<int>& dp) {
    if (n == 0) return 0;
    if (dp[n] != -1) return dp[n];
    int left = dpFrogJump(n - 1, height, dp) + abs(height[n] - height[n - 1]);
    int right = INT_MAX;
    if (n > 1) {
        right = dpFrogJump(n - 2, height, dp) + abs(height[n] - height[n - 2]);
    }
    return dp[n] = min(left, right);
}

int tabulationFrogJump(int n, const vector<int>& height) {
    vector<int> dp(n + 1, 0);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        int left = dp[i - 1] + abs(height[i] - height[i - 1]);
        int right = INT_MAX;
        if (i > 1) {
            right = dp[i - 2] + abs(height[i] - height[i - 2]);
        }
        dp[i] = min(left, right);
    }
    return dp[n];
}

int optimizedFrogJump(int n, const vector<int>& height) {
    int prev1 = 0; // dp[i-1]
    int prev2 = 0; // dp[i-2]
    for (int i = 1; i <= n; i++) {
        int left = prev1 + abs(height[i] - height[i - 1]);
        int right = INT_MAX;
        if (i > 1) {
            right = prev2 + abs(height[i] - height[i - 2]);
        }
        int current = min(left, right);
        prev2 = prev1;
        prev1 = current;
    }
    return prev1;
}

int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }
    vector<int> dp(n + 1, -1);
    cout << "Minimum energy required using recursion: " << recursiveFrogJump(n - 1, height) << endl;
    cout << "Minimum energy required using dynamic programming: " << dpFrogJump(n - 1, height, dp) << endl;
    cout << "Minimum energy required using tabulation: " << tabulationFrogJump(n - 1, height) << endl;
    cout << "Minimum energy required using optimization: " << optimizedFrogJump(n - 1, height) << endl;
    return 0;
}