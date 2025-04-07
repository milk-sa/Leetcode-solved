class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]
        kelvin=celsius+273.15
        Fahrenheit=celsius*1.8+32.00
        ans.append(kelvin)
        ans.append(Fahrenheit)

        return ans
        
        