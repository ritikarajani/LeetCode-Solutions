#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        for i in range(n):
            for j in range(i+1, n):
                if (-1 * (arr[i]+arr[j])) in arr[j+1:n]:
                    return 1
        return 0
    
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends