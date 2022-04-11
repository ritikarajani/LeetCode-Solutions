#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
       count = 0
       mdict ={}
       
       for num in arr:
           target = k- num
           if target in mdict:
               count += mdict[target]
           
           if num not in mdict:
               mdict[num] = 1
           else:
               mdict[num] += 1
       
       return count
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends