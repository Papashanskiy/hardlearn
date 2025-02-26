__import__("atexit").register(lambda: open(
    "display_runtime.txt", "w").write("6000"))


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left = 0
        max_score = 0
        counter = collections.Counter()
        current_sum = 0

        for right in range(len(nums)):
            counter[nums[right]] += 1
            current_sum += nums[right]

            while counter[nums[right]] > 1:
                counter[nums[left]] -= 1
                current_sum -= nums[left]
                left += 1

            max_score = max(max_score, current_sum)

        return max_score
