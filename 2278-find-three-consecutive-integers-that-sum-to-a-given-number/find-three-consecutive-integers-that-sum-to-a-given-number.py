class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        arr = []
        z = "There's no way to express "+str(num)+"as sum of 3 consecutive integers"
        if num%3 == 0:
            x=int(num/3)
            arr.append(x-1)
            arr.append(x)
            arr.append(x+1)
            return arr
        else:
            return arr
            
          

                


        