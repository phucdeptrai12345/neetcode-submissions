class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={};
        for i,n in enumerate(nums):
            count[n]=i;
        for i,n in enumerate(nums):
            u=target-n;
            if u in count and count[u]!=i:
                return [i,count[u]]
