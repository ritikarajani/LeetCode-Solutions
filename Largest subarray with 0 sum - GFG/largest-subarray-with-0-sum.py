#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
       d={}
       sum=0
       maxL=0
       for i in range(len(arr)):
           sum+=arr[i]
           if sum==0:
               maxL=i+1
           # print(d)
           # print(d.get(curr))
           
           
           if (sum not in d.keys()):
              
               d[sum]=i
           else:
               diff=i-d[sum]
               maxL=max(diff,maxL)
               
       
       return maxL    
        #Code here

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends