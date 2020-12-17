#Assume you have an array of length n initialized with all 0's and are given k update operations. 
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc. 
#
# Return the modified array after all k operations were executed. 
#
# Example: 
#
# 
#Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
#Output: [-2,0,3,5,3]
# 
#
# Explanation: 
#
# 
#Initial state:
#[0,0,0,0,0]
#
#After applying operation [1,3,2]:
#[0,2,2,2,0]
#
#After applying operation [2,4,3]:
#[0,2,5,5,3]
#
#After applying operation [0,2,-2]:
#[-2,0,3,5,3]
# Related Topics Array



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        if length == 0: return []
        n = len(updates)
        if n==0: return [0]*length
        arr = [0] *(length+1)
        for i in range(n):
            start, end, val = updates[i]
            arr[start] += val
            arr[end+1] -= val
        for i in range(1,length+1):
            arr[i] += arr[i-1]
        return arr[:length]

#leetcode submit region end(Prohibit modification and deletion)
