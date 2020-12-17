#You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope. 
#
# What is the maximum number of envelopes can you Russian doll? (put one inside other) 
#
# Note: 
#Rotation is not allowed. 
#
# Example: 
#
# 
# 
#Input: [[5,4],[6,4],[6,7],[2,3]]
#Output: 3 
#Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# 
# 
# Related Topics Binary Search Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        n = len(envelopes)
        arr = []

        for i in range(n):
            k = len(arr)
            low = 0
            high = k -1
            while low<=high:
                mid = low + (high-low)//2
                if arr[mid]>=envelopes[i][1]: high = mid -1
                else: low = mid +1
            if low==k: arr.append(envelopes[i][1])
            else: arr[low] = envelopes[i][1]
        return len(arr)


#leetcode submit region end(Prohibit modification and deletion)
