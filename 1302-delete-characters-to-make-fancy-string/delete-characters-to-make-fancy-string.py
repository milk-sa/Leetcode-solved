class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        count = 1
        ans = s[0]
        for i in range(1,len(s)):
            if s[i] == prev:
                prev = s[i]
                count+=1
            else:
                prev = s[i]
                count = 1
            if count<3:
                ans+=s[i]
        return ans
               
                    
        return ret