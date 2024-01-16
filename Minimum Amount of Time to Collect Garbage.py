from typing import List

class Solution(object):
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        prefixSum = [0] * len(travel)

        prefixSum[0] = travel[0]

        if len(travel) > 1 :
            for i in range(1, len(travel)):
                prefixSum[i] = prefixSum[i-1] + travel[i]

        garbageLastPositon = [-1,-1,-1]
        grabageCount = [0,0,0]
        for i, item in enumerate(garbage):

            if "M" in item:
                garbageLastPositon[0] = i

            if "P" in item:
                garbageLastPositon[1] = i

            if "G" in item:
                garbageLastPositon[2] = i


            grabageCount[0] += item.count("M")
            grabageCount[1] += item.count("P")
            grabageCount[2] += item.count("G")

        timeForM = prefixSum[garbageLastPositon[0] - 1] + grabageCount[0] if grabageCount[0] > 0 else grabageCount[0]
        timeForP = prefixSum[garbageLastPositon[1] - 1] + grabageCount[1] if grabageCount[1] > 0 else grabageCount[1]
        timeForG = prefixSum[garbageLastPositon[2] - 1] + grabageCount[2] if grabageCount[2] > 0 else grabageCount[2]

        totalTime = timeForM + timeForP + timeForG

        return totalTime



sol = Solution()

garbage = ["G", "P", "GP", "GG"]
travel = [2,4,3]

res = sol.garbageCollection(garbage,travel)

print(res)