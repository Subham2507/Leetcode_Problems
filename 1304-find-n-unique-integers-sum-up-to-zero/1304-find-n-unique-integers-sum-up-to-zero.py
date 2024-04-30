class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        for i in range(1,n//2+1):
            l.append(i)
            l.append(-i)
        if (n%2!=0):
            l.append(0)
        l.sort()
        return l