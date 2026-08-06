def count_strings(n):
    chars = ['a', 'b', 'c', 'd']

    forbidden = {
        ('a', 'b'),
        ('b', 'a'),
        ('b', 'c'),
        ('c', 'b')
    }

    idx = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

    # dp[position][parity][last]
    dp = [[[0] * 4 for _ in range(2)] for _ in range(n + 1)]

    # First character
    for ch in chars:
        parity = 1 if ch == 'a' else 0
        dp[1][parity][idx[ch]] = 1

    for pos in range(1, n):
        for parity in range(2):
            for last in range(4):
                cur = dp[pos][parity][last]
                if cur == 0:
                    continue

                last_char = chars[last]

                for nxt in chars:
                    if (last_char, nxt) in forbidden:
                        continue

                    new_parity = parity
                    if nxt == 'a':
                        new_parity ^= 1

                    dp[pos + 1][new_parity][idx[nxt]] += cur

    ans = 0
    for last in range(4):
        ans += dp[n][1][last]      # odd number of 'a'

    return ans


n = int(input())
print(count_strings(n))