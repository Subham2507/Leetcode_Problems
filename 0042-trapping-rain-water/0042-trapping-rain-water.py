def left_max(height,n):
    l1=[0 for x in range(n)]
    l1[0]=height[0]
    for i in range(1,n):
        l1[i]=max(l1[i-1],height[i])
    #print(l1)
    return l1
def right_max(height,n):
    l2=[0 for x in range(n)]
    l2[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        l2[i]=max(l2[i+1],height[i])
    print(l2)
        
    return l2
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        s=0
        l_left=left_max(height,n)
        l_right=right_max(height,n)
        
        #print(l_right)
        for i in range(1,n-1):
            s=s+min(l_right[i],l_left[i])-height[i]
        return s
        