#include<bits/stdc++.h>
using namespace std;

bool canPartition(int n, int target, vector<int>& arr) {
    vector<bool> prev(target + 1, 0), curr(target + 1, 0);
    prev[0] = curr[0] = true;
    if (arr[0] <= target) {
        prev[arr[0]] = true;
    }
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
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
        totalSum += arr[i];
    }
    if (totalSum % 2 != 0) {
        cout << "false" << endl;
        return 0;
    }
    int target = totalSum / 2;
    if (canPartition(n, target, arr)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    return 0;
}