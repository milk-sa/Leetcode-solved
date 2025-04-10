class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        lcm = (2 * n) // math.gcd(2, n)   
        return lcm
         

            
        