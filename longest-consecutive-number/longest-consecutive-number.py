def longestConsecutive1(nums):# 27/76
    s = sorted(nums)
    count = 0
    if s:
        for i in range(len(s)-1):
            if s[i]+1 == s[i+1]:
                count += 1
        return count+1
    return 0


def longestConsecutive2(nums):  # pass
    numset = set(nums)
    longest = 0
    for n in numset:
        if n-1 not in numset:
            length = 0
            while n+length in numset:
                length += 1
            longest = max(length, longest)
    return longest





if __name__ == "__main__":
    longestConsecutive2([1, 2, 4, 5, 6, 100, 300])
