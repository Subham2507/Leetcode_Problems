class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        l=[]
        for i in range(n//2):
            l.append(nums[i]+nums[-i-1])
        return max(l)