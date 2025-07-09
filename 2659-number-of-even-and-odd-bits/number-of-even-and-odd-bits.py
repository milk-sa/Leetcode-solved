class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = bin(n)[2:]
        rev = binary[::-1]
        print(rev)
        even = odd = 0 
        for i in range(len(rev)):
            if i%2 == 0 and int(rev[i]) == 1:
                even+=1
            elif i%2 != 0 and int(rev[i]) == 1: 
                odd+=1
        return [even,odd]           

        