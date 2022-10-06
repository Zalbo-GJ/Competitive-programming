class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        mod = 10**9+7
        arr.sort()
        
        for i in range(len(arr)):
            x = target - arr[i]
            j,k = i+1,len(arr)-1
            
            while j<k:
                if arr[j]+arr[k] < x:
                    j+=1
                elif arr[j]+arr[k]> x:
                    k-=1
                elif arr[j] != arr[k]:
                    l = r = 1
                    while j+1 <k and arr[j]==arr[j+1]:
                        l+=1
                        j+=1
                    while k-1 > j and arr[k] == arr[k-1]:
                        r+=1
                        k-=1
                    
                    ans += l*r
                    ans %= mod
                    j+=1
                    k-=1
                else:
                    ans += (k-j+1)* (k-j)/2
                    ans %= mod
                    break
        return ans