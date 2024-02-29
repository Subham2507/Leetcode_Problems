class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1={}
        for num in arr:
            dict1[num]=dict1.get(num,0)+1
        return len(set(dict1.values()))==len(dict1.values())
        