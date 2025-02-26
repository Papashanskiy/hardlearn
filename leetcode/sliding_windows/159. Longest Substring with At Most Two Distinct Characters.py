import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_length = 0
        left = 0
        counter = collections.Counter()

        for right in range(len(s)):
            counter[s[right]] += 1

            while len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
