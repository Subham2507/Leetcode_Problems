
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        l1=[]
        for i in range(n-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            n1=nums[i]
            target=-n1
            start=i+1
            end=n-1
            while(start<end):
                if(nums[start]+nums[end]<target):
                    start=start+1
                elif(nums[start]+nums[end]>target):
                    end=end-1
                else:
                    while(start<n-1 and nums[start]==nums[start+1]):
                        start=start+1
                    while(end>0 and nums[end]==nums[end-1]):
                        end=end-1
                    l1.append([n1,nums[start],nums[end]])
                    start=start+1
                    end=end-1
        return l1
        