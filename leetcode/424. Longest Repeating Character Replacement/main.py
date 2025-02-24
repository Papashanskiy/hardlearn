
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        max_length = 0
        count = {}
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
