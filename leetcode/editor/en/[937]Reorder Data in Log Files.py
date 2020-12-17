# You have an array of logs. Each log is a space delimited string of words. 
# 
#  For each log, the first word in each log is an alphanumeric identifier. Then,
#  either: 
# 
#  
#  Each word after the identifier will consist only of lowercase letters, or; 
#  Each word after the identifier will consist only of digits. 
#  
# 
#  We will call these two varieties of logs letter-logs and digit-logs. It is gu
# aranteed that each log has at least one word after its identifier. 
# 
#  Reorder the logs so that all of the letter-logs come before any digit-log. Th
# e letter-logs are ordered lexicographically ignoring identifier, with the identi
# fier used in case of ties. The digit-logs should be put in their original order.
#  
# 
#  Return the final order of the logs. 
# 
#  
#  Example 1: 
#  Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","l
# et3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig
# 2 3 6"]
#  
#  
#  Constraints: 
# 
#  
#  0 <= logs.length <= 100 
#  3 <= logs[i].length <= 100 
#  logs[i] is guaranteed to have an identifier, and a word after the identifier.
#  
#  
#  Related Topics String


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []
        contents = []
        for i, log in enumerate(logs):
            arr = log.split(" ")
            if arr[1].isdigit():
                digit_logs.append(log)
            else:
                content = ' '.join(arr[1:])
                contents.append((content, arr[0], i))
        contents.sort()
        for content, identifier, i in contents:
            letter_logs.append(logs[i])
        letter_logs.extend(digit_logs)
        return letter_logs

# leetcode submit region end(Prohibit modification and deletion)
