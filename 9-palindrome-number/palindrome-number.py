class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str=str(x)
        li=list(num_str)
        ans=[]
        for i in range(len(li)-1,-1,-1):
            ans.append(li[i])
        ans_str=''.join(ans) 
        if(num_str==ans_str):
            return True

        else:
            return False
                
            
        