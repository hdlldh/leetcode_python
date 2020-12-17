#Write a function that takes a string as input and reverse only the vowels of a string. 
#
# Example 1: 
#
# 
#Input: "hello"
#Output: "holle"
# 
#
# 
# Example 2: 
#
# 
#Input: "leetcode"
#Output: "leotcede" 
# 
#
# Note: 
#The vowels does not include the letter "y". 
#
# 
# Related Topics Two Pointers String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n==0: return s
        vowels = ['a','e','i','o','u']
        ans = list(s)
        i = 0
        j = n-1
        while i<j:
            while i<j and s[i].lower() not in vowels:
                i += 1
            while i<j and s[j].lower() not in vowels:
                j -= 1
            if i<j:
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1

        return ''.join(ans)


        
#leetcode submit region end(Prohibit modification and deletion)
