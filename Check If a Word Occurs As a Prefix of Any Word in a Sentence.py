class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """

        words = sentence.split()

        for index,word in enumerate(words,1):
            if word.startswith(searchWord):
                return index
        return -1


sol = Solution()
res = sol.isPrefixOfWord("i love eating burger","burg")
print(res)
