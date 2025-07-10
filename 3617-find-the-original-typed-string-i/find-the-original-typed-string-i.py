class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        output = 1
        
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                output +=1
            
        return output