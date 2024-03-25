class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest_sum=100000
        for k in range(0,n-2):
            i=k+1
            j=n-1
            while(i<j):
                sum_1=nums[i]+nums[j]+nums[k]
                if (abs(target-sum_1))<(abs(target-closest_sum)):
                    closest_sum=sum_1
                if(sum_1<target):
                    i=i+1
                else:
                    j=j-1
        
        return closest_sum   