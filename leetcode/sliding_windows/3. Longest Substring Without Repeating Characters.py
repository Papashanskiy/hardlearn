import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = collections.Counter()
        left = 0
        max_length = 0
        for right in range(len(s)):
            counter[s[right]] += 1

            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
