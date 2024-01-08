from typing import List

class Solution(object):
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        k = []
        count = 0

        for i in queries:
            x1 = i[0]
            y1 = i[1]
            r = i[2]

            for j in points:
                x2 = j[0]
                y2 = j[1]

                if (((x2-x1)**2 + (y2-y1)**2)**0.5) <= r:
                    count += 1

            k.append(count)

            count = 0

        return k

sol = Solution()
res = sol.countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]])
print(res)
