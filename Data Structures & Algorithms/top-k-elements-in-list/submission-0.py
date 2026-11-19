class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element = {}

        for i in nums:
            if i not in element:
                element[i] = 1
            else:
                element[i] += 1

        result = sorted(element, key=element.get, reverse=True)

        return result[:k]