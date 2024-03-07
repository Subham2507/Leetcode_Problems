
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        l1=[]
        for i in range(n-2):  ###Make it 3sum to 2 sum
            if(i>0 and nums[i]==nums[i-1]): ### If the previous and current value are same skip it
                continue
            n1=nums[i] ### new target for 2 sum
            target=-n1
            start=i+1
            end=n-1
            while(start<end):
                if(nums[start]+nums[end]<target):
                    start=start+1
                elif(nums[start]+nums[end]>target):
                    end=end-1
                else:
                    while(start<n-1 and nums[start]==nums[start+1]): ## skip one term for same value
                        start=start+1
                    while(end>0 and nums[end]==nums[end-1]):
                        end=end-1
                    l1.append([n1,nums[start],nums[end]])
                    start=start+1
                    end=end-1
        return l1
        