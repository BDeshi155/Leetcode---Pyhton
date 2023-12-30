from typing import List

class Solution(object):
    def countPairs(self, nums: List[int], target:int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        nums.sort()

        c = 0
        l = 0
        r = n-1

        while l<r:
            if nums[l] + nums[r] < target:
                c += r - l
                l += 1

            else:
                r -= 1

        return c

sol = Solution()
res = sol.countPairs([-1,1,2,3,1],2)
print(res)

