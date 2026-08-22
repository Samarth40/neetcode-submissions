class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char,0) + 1
        for i in range(len(s2)):
            for j in range(i+1,len(s2)+1):
                substring = s2[i:j]

                if len(substring) !=len(s1):
                    continue
                count2 = {}
                for char in substring:
                    count2[char] = count2.get(char,0) + 1
                
                if count1 == count2:
                    return True
        return False
