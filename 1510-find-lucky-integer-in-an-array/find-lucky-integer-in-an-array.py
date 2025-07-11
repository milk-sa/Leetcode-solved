class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        output = []
        dic = {}
        for i in range(len(arr)-1,-1,-1):
            if arr[i] in dic:
                dic[arr[i]] +=1
            else:
                dic[arr[i]] = 1
        
        for key, value in dic.items():
            if key == value:
                output.append(key)    
        return max(output) if output else -1