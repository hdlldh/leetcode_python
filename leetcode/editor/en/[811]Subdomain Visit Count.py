# A website domain like "discuss.leetcode.com" consists of various subdomains. A
# t the top level, we have "com", at the next level, we have "leetcode.com", and a
# t the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss
# .leetcode.com", we will also visit the parent domains "leetcode.com" and "com" i
# mplicitly. 
# 
#  Now, call a "count-paired domain" to be a count (representing the number of v
# isits this domain received), followed by a space, followed by the address. An ex
# ample of a count-paired domain might be "9001 discuss.leetcode.com". 
# 
#  We are given a list cpdomains of count-paired domains. We would like a list o
# f count-paired domains, (in the same format as the input, and in any order), tha
# t explicitly counts the number of visits to each subdomain. 
# 
#  
# Example 1:
# Input: 
# ["9001 discuss.leetcode.com"]
# Output: 
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
# Explanation: 
# We only have one website domain: "discuss.leetcode.com". As discussed above, t
# he subdomain "leetcode.com" and "com" will also be visited. So they will all be 
# visited 9001 times.
# 
#  
# 
#  
# Example 2:
# Input: 
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: 
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 i
# ntel.mail.com","951 com"]
# Explanation: 
# We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.c
# om" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 90
# 0 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
# 
#  
# 
#  Notes: 
# 
#  
#  The length of cpdomains will not exceed 100. 
#  The length of each domain name will not exceed 100. 
#  Each address will have either 1 or 2 "." characters. 
#  The input count in any count-paired domain will not exceed 10000. 
#  The answer output can be returned in any order. 
#  
#  Related Topics Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        hashmap = collections.defaultdict(int)
        for domain in cpdomains:
            cnt, name = domain.split(' ')
            cnt = int(cnt)
            name_list = name.split('.')
            for i in range(len(name_list)):
                sub_name = '.'.join(name_list[i:])
                hashmap[sub_name] += cnt
        ans = []
        for k, v in hashmap.items():
            ans.append(str(v) + " " + k)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
