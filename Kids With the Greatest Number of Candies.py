from typing import List

class Solution(object):
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandies = max(candies)
        res = []

        for candy in candies:
            if candy + extraCandies >= maxCandies:
                res.append(True)

            else:
                res.append(False)

        return res


if __name__ ==  "__main__" :
    sol = Solution()
    #candies = [2,3,5,1,3]
    candies = [4,2,1,1,2]
    extracandies = 1

    result = sol.kidsWithCandies(candies,extracandies)
    print(result)
