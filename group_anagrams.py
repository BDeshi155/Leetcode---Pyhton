from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)

        return result


if __name__ == "__main__":
    solution = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output_result = solution.groupAnagrams(input_strs)
    print(output_result)