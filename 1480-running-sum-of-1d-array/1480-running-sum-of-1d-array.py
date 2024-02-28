class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        sum_1=0
        for i in nums:
            sum_1=sum_1+i
            l.append(sum_1)
        return l
        