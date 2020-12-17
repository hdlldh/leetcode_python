# You are given some lists of regions where the first region of each list includ
# es all other regions in that list. 
# 
#  Naturally, if a region X contains another region Y then X is bigger than Y. A
# lso by definition a region X contains itself. 
# 
#  Given two regions region1, region2, find out the smallest region that contain
# s both of them. 
# 
#  If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaran
# teed there is no r2 such that r2 includes r3. 
#  
# It's guaranteed the smallest region exists. 
# 
#  
#  Example 1: 
# 
#  
# Input:
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# Output: "North America"
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= regions.length <= 10^4 
#  region1 != region2 
#  All strings consist of English letters and spaces with at most 20 letters. 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        
# leetcode submit region end(Prohibit modification and deletion)
