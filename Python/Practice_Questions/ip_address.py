def restoreIPAddresses(s):
    res = []

    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            res.append('.'.join(path))
            return

        if len(path) >= 4:
            return

        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start + length]
            if (segment[0] == '0' and length > 1) or (length == 3 and int(segment) > 255):
                continue
            backtrack(start + length, path + [segment])

    backtrack(0, [])
    return res

# Example Usage:
s = "25525511135"
print(restoreIPAddresses(s))