#Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *. 
#
# Example 1: 
#
# 
#Input: "2-1-1"
#Output: [0, 2]
#Explanation: 
#((2-1)-1) = 0 
#(2-(1-1)) = 2 
#
# Example 2: 
#
# 
#Input: "2*3-4*5"
#Output: [-34, -14, -10, -10, 10]
#Explanation: 
#(2*(3-(4*5))) = -34 
#((2*3)-(4*5)) = -14 
#((2*(3-4))*5) = -10 
#(2*((3-4)*5)) = -10 
#(((2*3)-4)*5) = 10
# Related Topics Divide and Conquer



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.helper(input, {})

    def helper(self, input, mem):
        if not input: return []
        if input in mem: return mem[input]
        ans = []
        for i in range(len(input)):
            if input[i] in ['+','-','*']:
                left = self.helper(input[:i], mem)
                right = self.helper(input[i+1:],mem)
                for ln in left:
                    for rn in right:
                        if input[i] == '+': ans.append(ln+rn)
                        elif input[i] == '-': ans.append(ln-rn)
                        else: ans.append(ln*rn)
        if not ans: ans.append(int(input))
        mem[input] = ans
        return ans


#leetcode submit region end(Prohibit modification and deletion)
