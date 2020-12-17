# Some people will make friend requests. The list of their ages is given and age
# s[i] is the age of the ith person. 
# 
#  Person A will NOT friend request person B (B != A) if any of the following co
# nditions are true: 
# 
#  
#  age[B] <= 0.5 * age[A] + 7 
#  age[B] > age[A] 
#  age[B] > 100 && age[A] < 100 
#  
# 
#  Otherwise, A will friend request B. 
# 
#  Note that if A requests B, B does not necessarily request A. Also, people wil
# l not friend request themselves. 
# 
#  How many total friend requests are made? 
# 
#  Example 1: 
# 
#  
# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
#  
# 
#  Example 2: 
# 
#  
# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17. 
# 
#  Example 3: 
# 
#  
# Input: [20,30,100,110,120]
# Output: 
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
#  
# 
#  
# 
#  Notes: 
# 
#  
#  1 <= ages.length <= 20000. 
#  1 <= ages[i] <= 120. 
#  
#  Related Topics Array


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = collections.Counter(ages)
        ans = 0
        for age1, count1 in count.items():
            for age2, count2 in count.items():
                if age2 <= age1 * 0.5 + 7: continue
                if age2 > age1: continue
                if age2 > 100 and age1 < 100: continue
                if age1 == age2:
                    ans += count1 * (count1 -1)
                    continue
                ans += count1*count2
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
