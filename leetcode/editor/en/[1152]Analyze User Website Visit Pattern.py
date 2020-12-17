# We are given some website visits: the user with name username[i] visited the w
# ebsite website[i] at time timestamp[i]. 
# 
#  A 3-sequence is a list of websites of length 3 sorted in ascending order by t
# he time of their visits. (The websites in a 3-sequence are not necessarily disti
# nct.) 
# 
#  Find the 3-sequence visited by the largest number of users. If there is more 
# than one solution, return the lexicographically smallest such 3-sequence. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: username = ["joe","joe","joe","james","james","james","james","mary","m
# ary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","car
# eer","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: 
# The tuples in this example are:
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# The 3-sequence ("home", "about", "career") was visited at least once by 2 user
# s.
# The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
# The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
# The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
# The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
#  
# 
#  
# 
#  Note: 
# 
#  
#  3 <= N = username.length = timestamp.length = website.length <= 50 
#  1 <= username[i].length <= 10 
#  0 <= timestamp[i] <= 10^9 
#  1 <= website[i].length <= 10 
#  Both username[i] and website[i] contain only lowercase characters. 
#  It is guaranteed that there is at least one user who visited at least 3 websi
# tes. 
#  No user visits two websites at the same time. 
#  
#  Related Topics Array Hash Table Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """

        history = collections.defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            history[u].append((t, w))

        counter = collections.defaultdict(int)
        visited = collections.defaultdict(set)
        for u, l in history.items():
            if len(l) < 3: continue
            l.sort()

            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    for k in range(j+1, len(l)):
                        key = '%s_%s_%s'%(l[i][1],l[j][1],l[k][1])
                        if key not in visited[u]:
                            counter[key] += 1
                            visited[u].add(key)

        max_count = 0
        ans = ''
        for k, v in counter.items():
            if v > max_count:
                max_count = v
                ans = k
            elif v == max_count and k < ans:
                ans = k
        return ans.split('_')
        
# leetcode submit region end(Prohibit modification and deletion)
