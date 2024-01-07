from typing import List

class Solution(object):
    def mostWordsFound(self, sentences: List[str]) -> int:
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans = 0


        for i in range(len(sentences)):
            sentences[i] = sentences[i].count(' ') + 1
            ans = max(ans,sentences[i])

        return ans


sol = Solution()
res1 = sol.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
res2 = sol.mostWordsFound(["please wait", "continue to fight", "continue to win"])
print(res2)