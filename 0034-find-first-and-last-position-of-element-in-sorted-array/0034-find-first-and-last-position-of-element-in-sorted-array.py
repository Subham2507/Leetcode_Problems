class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=0
        end=len(nums) - 1
        ans=-1
        while(start<=end):
            mid=start+(end-start)//2
            if(nums[mid]==target):
                ans=mid
                end=mid-1
            elif(nums[mid]>target):## left me jao bhai
                end=mid-1
            else:##right mein jao bhai
                start=mid+1
                
        start_1=0
        end_1=len(nums) - 1
        ans_1=-1
        while(start_1<=end_1):
            mid_1=start_1+(end_1-start_1)//2
            if(nums[mid_1]==target):
                ans_1=mid_1
                start_1=mid_1+1
            elif(nums[mid_1]>target):## left me jao bhai
                end_1=mid_1-1
            else:##right mein jao bhai
                start_1=mid_1+1
        return [ans,ans_1]