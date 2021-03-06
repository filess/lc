class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter()
        for c in s:
            counter[c] += 1
        cnt = 0
        for val in counter.values():
            if (val & 1) == 1:
                cnt += 1
            if cnt > 1:
                return False
        return True
