#On a single threaded CPU, we execute some functions. Each function has a unique
# id between 0 and N-1. 
#
# We store logs in timestamp order that describe when a function is entered or e
#xited. 
#
# Each log is a string with this format: "{function_id}:{"start" | "end"}:{times
#tamp}". For example, "0:start:3" means the function with id 0 started at the beg
#inning of timestamp 3. "1:end:2" means the function with id 1 ended at the end o
#f timestamp 2. 
#
# A function's exclusive time is the number of units of time spent in this funct
#ion. Note that this does not include any recursive calls to child functions. 
#
# The CPU is single threaded which means that only one function is being execute
#d at a given time unit. 
#
# Return the exclusive time of each function, sorted by their function id. 
#
# 
#
# Example 1: 
#
# 
#
# 
#Input:
#n = 2
#logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
#Output: [3, 4]
#Explanation:
#Function 0 starts at the beginning of time 0, then it executes 2 units of time 
#and reaches the end of time 1.
#Now function 1 starts at the beginning of time 2, executes 4 units of time and 
#ends at time 5.
#Function 0 is running again at the beginning of time 6, and also ends at the en
#d of time 6, thus executing for 1 unit of time. 
#So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 sp
#ends 4 units of total time executing.
# 
#
# 
#
# Note: 
#
# 
# 1 <= n <= 100 
# Two functions won't start or end at the same time. 
# Functions will always log when they exit. 
# 
#
# 
# Related Topics Stack




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        prev = None
        ans = [0]*n
        stack = []
        for log in logs:
            log_arr= log.split(':')
            fid = int(log_arr[0])
            action = log_arr[1]
            cur = int(log_arr[2])
            if action[0]=='s':
                if stack: ans[stack[-1]] += cur - prev
                stack.append(fid)
                prev = cur
            else:
                ans[stack[-1]] += cur - prev +1
                stack.pop()
                prev = cur+1
        return ans
        
#leetcode submit region end(Prohibit modification and deletion)
