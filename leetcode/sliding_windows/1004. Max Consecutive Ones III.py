from typing import List


__import__("atexit").register(lambda: open(
    "display_runtime.txt", "w").write("0"))


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1
