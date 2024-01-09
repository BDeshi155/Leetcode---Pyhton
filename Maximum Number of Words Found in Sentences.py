from typing import List


class Solution:
    def mostWordsFound(self, sentences):
        max_len = 0

        for curr_sent in sentences:
            word_list = curr_sent.split(" ")

            curr_len = len(word_list)

            if max_len < curr_len:
                max_len = curr_len

        return max_len


sol = Solution()
res1 = sol.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
res2 = sol.mostWordsFound(["please wait", "continue to fight", "continue to win"])
print(res1)