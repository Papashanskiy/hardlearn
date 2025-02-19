from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        if not nums:
            return 0
        nums.sort()
        try:
            idx = nums.index(val)
        except ValueError:
            return 0
        for i in range(idx, len(nums)):
            if nums[i] == val:
                nums[i] = 51
                k += 1
            else:
                break
        nums.sort()
        return len(nums) - k
    

if __name__ == '__main__':
    s = Solution()
    s.removeElement([2], 3)
