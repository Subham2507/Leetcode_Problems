def left_max(height,n):
    '''Find out the left max element for each number in array'''
    l1=[0 for x in range(n)]
    l1[0]=height[0]
    for i in range(1,n):
        l1[i]=max(l1[i-1],height[i])
    return l1
def right_max(height,n):
    '''Find out the right max element for each number in array'''
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
        l_left=left_max(height,n) ## call the function
        l_right=right_max(height,n)
        for i in range(1,n-1):####As we don't need the boundary condition here
            s=s+min(l_right[i],l_left[i])-height[i] ### volume of water for each width
        return s
        