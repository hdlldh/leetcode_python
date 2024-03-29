#Given a chemical formula (given as a string), return the count of each atom.
# 
#An atomic element always starts with an uppercase character, then zero or more 
#lowercase letters, representing the name.
# 
#1 or more digits representing the count of that element may follow if the count
# is greater than 1. If the count is 1, no digits will follow. For example, H2O a
#nd H2O2 are possible, but H1O2 is impossible.
# 
#Two formulas concatenated together produce another formula. For example, H2O2He
#3Mg4 is also a formula. 
# 
#A formula placed in parentheses, and a count (optionally added) is also a formu
#la. For example, (H2O2) and (H2O2)3 are formulas.
# 
#Given a formula, output the count of all elements as a string in the following 
#form: the first name (in sorted order), followed by its count (if that count is 
#more than 1), followed by the second name (in sorted order), followed by its cou
#nt (if that count is more than 1), and so on. 
#
# Example 1: 
# 
#Input: 
#formula = "H2O"
#Output: "H2O"
#Explanation: 
#The count of elements are {'H': 2, 'O': 1}.
# 
# 
#
# Example 2: 
# 
#Input: 
#formula = "Mg(OH)2"
#Output: "H2MgO2"
#Explanation: 
#The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# 
# 
#
# Example 3: 
# 
#Input: 
#formula = "K4(ON(SO3)2)2"
#Output: "K4N2O14S4"
#Explanation: 
#The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# 
# 
#
# Note:
# All atom names consist of lowercase letters, except for the first character wh
#ich is uppercase. 
# The length of formula will be in the range [1, 1000]. 
# formula will only consist of letters, digits, and round parentheses, and is a 
#valid formula as defined in the problem. 
# Related Topics Hash Table Stack Recursion




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        self.i = 0
        counts = self.helper(formula)
        ans = ''
        for k in sorted(counts.keys()):
            ans += k
            if counts[k]>1: ans+= str(counts[k])
        return ans


    def helper(self, formula):
        counts = collections.defaultdict(int)
        while self.i < len(formula):
            ch = formula[self.i]
            if ch == '(':
                self.i+=1
                tmp_counts = self.helper(formula)
                count = self.getCount(formula)
                for k, v in tmp_counts.items():
                    counts[k] += v*count
            elif ch == ')':
                self.i+=1
                return counts
            else:
                name = self.getName(formula)
                counts[name] += self.getCount(formula)
        return counts

    def getName(self, formula):
        name = formula[self.i]
        self.i+=1
        while (self.i<len(formula) and 'a'<=formula[self.i]<='z'):
            name += formula[self.i]
            self.i+=1
        return name

    def getCount(self, formula):
        count = 0
        while (self.i<len(formula) and '0'<=formula[self.i]<='9'):
            count = count*10 + ord(formula[self.i]) -ord('0')
            self.i+=1
        if count ==0: return 1
        return count

        
#leetcode submit region end(Prohibit modification and deletion)
