#include<bits/stdc++.h>
using namespace std;

// memoization approach to calculate nth Fibonacci number
// time complexity: O(n)
// space complexity: O(n) + O(n) for recursion stack

int fibo(int n, vector<int>& dp) {
    if (n <= 1) {
        return n;
    }
    if (dp[n] != -1) {
        return dp[n];
    }
    return dp[n] = fibo(n - 1, dp) + fibo(n - 2, dp);
}

// tabulation approach to calculate nth Fibonacci number
// time complexity: O(n)
// space complexity: O(n)
int fiboTab(int n) {
    vector<int> dp(n + 1, 0);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[n];
}

// Optimized space approach to calculate nth Fibonacci number
// time complexity: O(n)
// space complexity: O(1)
int fiboOpt(int n) {
    if (n <= 1) {
        return n;
    }
    int curr = 0, prev = 1, c;
    for (int i = 2; i <= n; i++) {
        c = curr + prev;
        curr = prev;
        prev = c;
    }
    return prev;
}

int main() {
    int n;
    cin >> n;
    vector<int> dp(n + 1, -1);
    cout << "Memoization: " << fibo(n, dp) << endl;
    cout << "Tabulation: " << fiboTab(n) << endl;
    cout << "Optimized Space: " << fiboOpt(n) << endl;
    return 0;
}