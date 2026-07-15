class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashDict = {}
        flag = False
        historic = []
        for i in nums:
            if i in HashDict:
                HashDict[i] += 1
            else:
                HashDict[i] = 1
        
        for x in HashDict:
            historic.append(HashDict[x])
        
        flag= any(i > 1 for i in historic)


        return flag
        