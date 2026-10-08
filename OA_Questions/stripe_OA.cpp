// You are given an integer N. Consider the set S of all distinct values of (x XOR y), 
// where x and y are positive integers such that 1 <= x, y <= N.
// Find the size of set S, i.e., the number of distinct XOR values possible.
// Since the answer can be very large, output it modulo 1,000,000,007 (10^9 + 7).

// 1<=N<=10^12 

#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;

// Modular exponentiation: (base^exp) % MOD
long long power(long long base, long long exp) {
    long long result = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    
    while (T--) {
        long long N;
        cin >> N;
        
        // Find highest set bit position
        int highestBitPos = 63 - __builtin_clzll(N);
        
        long long answer;
        
        if (N == 2) {
            answer = 2;
        }
        else if ((N & (N - 1)) == 0) {
            // N is a power of 2
            // answer = 2^(highestBitPos+1) - 1
            answer = (power(2, highestBitPos + 1) - 1 + MOD) % MOD;
        } else {
            // Non power of 2
            // answer = 2^(highestBitPos+1)
            answer = power(2, highestBitPos + 1);
        }
        
        cout << answer << "\n";
    }
    
    return 0;
}
