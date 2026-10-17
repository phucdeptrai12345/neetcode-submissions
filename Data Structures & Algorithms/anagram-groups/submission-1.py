class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count=defaultdict(list)
        for i in strs:
            count[tuple(sorted(i))].append(i)
        return list(count.values())