# We have a sequence of books: the i-th book has thickness books[i][0] and heigh
# t books[i][1]. 
# 
#  We want to place these books in order onto bookcase shelves that have total w
# idth shelf_width. 
# 
#  We choose some of the books to place on this shelf (such that the sum of thei
# r thickness is <= shelf_width), then build another level of shelf of the bookcas
# e so that the total height of the bookcase has increased by the maximum height o
# f the books we just put down. We repeat this process until there are no more boo
# ks to place. 
# 
#  Note again that at each step of the above process, the order of the books we 
# place is the same order as the given sequence of books. For example, if we have 
# an ordered list of 5 books, we might place the first and second book onto the fi
# rst shelf, the third book on the second shelf, and the fourth and fifth book on 
# the last shelf. 
# 
#  Return the minimum possible height that the total bookshelf can be after plac
# ing shelves in this manner. 
# 
#  
#  Example 1: 
# 
#  
# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= books.length <= 1000 
#  1 <= books[i][0] <= shelf_width <= 1000 
#  1 <= books[i][1] <= 1000 
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
