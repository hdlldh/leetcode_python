# Write an iterator that iterates through a run-length encoded sequence. 
# 
#  The iterator is initialized by RLEIterator(int[] A), where A is a run-length 
# encoding of some sequence. More specifically, for all even i, A[i] tells us the 
# number of times that the non-negative integer value A[i+1] is repeated in the se
# quence. 
# 
#  The iterator supports one function: next(int n), which exhausts the next n el
# ements (n >= 1) and returns the last element exhausted in this way. If there is 
# no element left to exhaust, next returns -1 instead. 
# 
#  For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding 
# of the sequence [8,8,8,5,5]. This is because the sequence can be read as "three 
# eights, zero nines, two fives". 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[
# 1],[2]]
# Output: [null,8,8,5,-1]
# Explanation: 
# RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
# This maps to the sequence [8,8,8,5,5].
# RLEIterator.next is then called 4 times:
# 
# .next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequenc
# e is now [8, 5, 5].
# 
# .next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence
#  is now [5, 5].
# 
# .next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence
#  is now [5].
# 
# .next(2) exhausts 2 terms, returning -1.  This is because the first term exhau
# sted was 5,
# but the second term did not exist.  Since the last term exhausted does not exi
# st, we return -1.
# 
#  
# 
#  Note: 
# 
#  
#  0 <= A.length <= 1000 
#  A.length is an even integer. 
#  0 <= A[i] <= 10^9 
#  There are at most 1000 calls to RLEIterator.next(int n) per test case. 
#  Each call to RLEIterator.next(int n) will have 1 <= n <= 10^9. 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.nums = A
        self.cur = 0
        #print(self.num, self.cnt)

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.cur < len(self.nums) and n > self.nums[self.cur]:
            #print(self.nums, self.cur)
            n -= self.nums[self.cur]
            self.cur += 2
        if self.cur>=len(self.nums): return -1
        self.nums[self.cur] -= n
        return self.nums[self.cur+1]



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
# leetcode submit region end(Prohibit modification and deletion)
