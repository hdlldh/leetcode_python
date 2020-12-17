#An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels. 
#
# Example: 
#
# 
#Input:
#[
#  "0010",
#  "0110",
#  "0100"
#]
#and x = 0, y = 2
#
#Output: 6
# 
# Related Topics Binary Search



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        top = self.searchRows(image, 0, x, True)
        bottom = self.searchRows(image, x, m-1, False)
        left = self.searchCols(image, 0, y, True)
        right = self.searchCols(image, y, n-1, False)
        return (bottom-top)*(right-left)

    def searchRows(self, image, low, high, white2black):
        m, n = len(image), len(image[0])
        while low<=high:
            mid = low +(high-low)//2
            print(low, high, mid)
            k = 0
            found = False
            while k<n:
                if image[mid][k]=='1':
                    found = True
                    break
                k+=1
            if white2black:
                if found: high = mid -1
                else: low = mid +1
            else:
                if found: low = mid + 1
                else: high = mid -1
        return low

    def searchCols(self, image, low, high, white2black):
        m, n = len(image), len(image[0])
        while low <= high:
            mid = low + (high - low) // 2
            k = 0
            found = False
            while k < m:
                if image[k][mid] == '1':
                    found = True
                    break
                k += 1
            if white2black:
                if found:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if found:
                    low = mid + 1
                else:
                    high = mid - 1
        return low
#leetcode submit region end(Prohibit modification and deletion)
