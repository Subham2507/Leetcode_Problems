class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        
        while(start<=end):
            mid= start + (end - start)//2 #Find out the mid point
            if(nums[mid]==target):
                return mid
            else:
                if target > nums[mid]:
                    start=mid+1##Going to the right part
                else:
                    end=mid-1 ## Going to the left part
        return -1
        