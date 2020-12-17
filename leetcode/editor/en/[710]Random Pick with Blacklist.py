# Given a blacklist B containing unique integers from [0, N), write a function t
# o return a uniform random integer from [0, N) which is NOT in B. 
# 
#  Optimize it such that it minimizes the call to system’s Math.random(). 
# 
#  Note: 
# 
#  
#  1 <= N <= 1000000000 
#  0 <= B.length < min(100000, N) 
#  [0, N) does NOT include N. See interval notation. 
#  
# 
#  Example 1: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# Output: [null,0,0,0]
#  
# 
#  Example 2: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# Output: [null,1,1,1]
#  
# 
#  Example 3: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
#  
# 
#  Example 4: 
# 
#  
# Input: 
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# Output: [null,1,3,1]
#  
# 
#  Explanation of Input Syntax: 
# 
#  The input is two lists: the subroutines called and their arguments. Solution'
# s constructor has two arguments, N and the blacklist B. pick has no arguments. A
# rguments are always wrapped with a list, even if there aren't any. 
#  Related Topics Hash Table Binary Search Sort Random


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        n = len(blacklist)
        self.len = N - n
        self.hashmap = {}
        i = N - n
        while i < N and i in blacklist: i+=1
        for num in blacklist:
            if num < self.len:
                self.hashmap[num] = i
                i += 1
                while i<N and i in blacklist: i+= 1


    def pick(self):
        """
        :rtype: int
        """
        n = random.randrange(self.len)
        if n in self.hashmap: return self.hashmap[n]
        return n



# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# leetcode submit region end(Prohibit modification and deletion)
