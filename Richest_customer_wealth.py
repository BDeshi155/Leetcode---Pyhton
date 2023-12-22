class Solution(object):
    def maximumWealth(self,accounts):
        """

        :type accounts:
        :rtype: int
        """

        wealth = list()
        for i in accounts:
            wealth.append(sum(i))

        return max(wealth)


example = [[1,2,9],[1,2,3]]

solution = Solution()

result = solution.maximumWealth(example)

print(result)