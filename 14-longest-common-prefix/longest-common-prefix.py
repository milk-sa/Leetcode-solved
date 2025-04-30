class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return_string = ""
        x=min(strs,key=len)
        y=len(x)
        res = ""
        for i in range(len(x)):
            
                if all(x[i] == s[i] for s in strs):
                   res+=x[i]
                else:
                
                    break   
            
        return res    

 
                
            

              
            
        
        
        