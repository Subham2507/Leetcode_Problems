class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            missing=arr[mid]-(mid+1) ## missing value coresponding to mid value
            if(missing < k): ## if missing value is less then k will move to right portion
                low=mid+1
            else:
                high=mid-1
        return k+high+1