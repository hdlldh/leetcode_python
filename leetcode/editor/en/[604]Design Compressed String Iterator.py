# 
# Design and implement a data structure for a compressed string iterator. It sho
# uld support the following operations: next and hasNext.
#  
# 
#  
# The given compressed string will be in the form of each letter followed by a p
# ositive integer representing the number of this letter existing in the original 
# uncompressed string.
#  
# 
#  
# next() - if the original string still has uncompressed characters, return the 
# next letter; Otherwise return a white space. 
# hasNext() - Judge whether there is any letter needs to be uncompressed.
#  
# 
#  
# Note: 
# Please remember to RESET your class variables declared in StringIterator, as s
# tatic/class variables are persisted across multiple test cases. Please see here 
# for more details.
#  
# 
# 
#  Example:
#  
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
# 
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '
#  
#  Related Topics Design


# leetcode submit region begin(Prohibit modification and deletion)
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.str = []
        self.cnt = []
        i = 0
        while i < len(compressedString):
            if compressedString[i]>='0' and compressedString[i]<='9':
                val = 0
                while i <len(compressedString) and compressedString[i]>='0' and compressedString[i]<='9':
                    val = 10*val + ord(compressedString[i]) - ord('0')
                    i += 1
                self.cnt.append(val)
            else:
                self.str.append(compressedString[i])
                i += 1
        #print(self.str, self.cnt)

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext(): return " "
        self.cnt[0] -= 1
        ans = self.str[0]
        if self.cnt[0] == 0:
            self.cnt.pop(0)
            self.str.pop(0)
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.str: return True
        return False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# leetcode submit region end(Prohibit modification and deletion)
