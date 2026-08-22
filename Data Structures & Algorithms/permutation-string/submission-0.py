class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_strs = []
        for i in range(0,len(s2)):
            for j in range(i+1,len(s2)+1):
                sub_strs.append(s2[i:j])
        for i in range(0,len(sub_strs)):
            if sorted(sub_strs[i]) == sorted(s1):
                return True
        
        return False