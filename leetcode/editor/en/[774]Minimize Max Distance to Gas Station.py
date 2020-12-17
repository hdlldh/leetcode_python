# On a horizontal number line, we have gas stations at positions stations[0], st
# ations[1], ..., stations[N-1], where N = stations.length. 
# 
#  Now, we add K more gas stations so that D, the maximum distance between adjac
# ent gas stations, is minimized. 
# 
#  Return the smallest possible value of D. 
# 
#  Example: 
# 
#  
# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000
#  
# 
#  Note: 
# 
#  
#  stations.length will be an integer in range [10, 2000]. 
#  stations[i] will be an integer in range [0, 10^8]. 
#  K will be an integer in range [1, 10^6]. 
#  Answers within 10^-6 of the true value will be accepted as correct. 
#  
#  Related Topics Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        def possible(D):
            cnt = 0
            for i in range(1,len(stations)):
                cnt += int((stations[i]-stations[i-1])/D)
            return cnt <= K
        low = 0
        high = 10**8
        while high-low > 10**-6:
            mid = low + (high-low)/2.0
            if possible(mid): high = mid
            else: low = mid
        return low

        
# leetcode submit region end(Prohibit modification and deletion)
