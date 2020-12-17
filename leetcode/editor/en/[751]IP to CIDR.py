# 
# Given a start IP address ip and a number of ips we need to cover n, return a r
# epresentation of the range as a list (of smallest possible length) of CIDR block
# s.
#  
# A CIDR block is a string consisting of an IP, followed by a slash, and then th
# e prefix length. For example: "123.45.67.89/20". That prefix length "20" represe
# nts the number of common prefix bits in the specified range.
#  
# 
#  Example 1: 
#  
# Input: ip = "255.0.0.7", n = 10
# Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
# Explanation:
# The initial ip address, when converted to binary, looks like this (spaces adde
# d for clarity):
# 255.0.0.7 -> 11111111 00000000 00000000 00000111
# The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 
# bits to the given address,
# ie. just this one address.
# 
# The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 
# bits to the given address:
# 255.0.0.8 -> 11111111 00000000 00000000 00001000
# Addresses with common prefix of 29 bits are:
# 11111111 00000000 00000000 00001000
# 11111111 00000000 00000000 00001001
# 11111111 00000000 00000000 00001010
# 11111111 00000000 00000000 00001011
# 11111111 00000000 00000000 00001100
# 11111111 00000000 00000000 00001101
# 11111111 00000000 00000000 00001110
# 11111111 00000000 00000000 00001111
# 
# The address "255.0.0.16/32" specifies all addresses with a common prefix of 32
#  bits to the given address,
# ie. just 11111111 00000000 00000000 00010000.
# 
# In total, the answer specifies the range of 10 ips starting with the address 2
# 55.0.0.7 .
# 
# There were other representations, such as:
# ["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
# but our answer was the shortest possible.
# 
# Also note that a representation beginning with say, "255.0.0.7/30" would be in
# correct,
# because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 0000
# 0100 
# that are outside the specified range.
#  
#  
# 
#  Note: 
#  
#  ip will be a valid IPv4 address. 
#  Every implied address ip + x (for x < n) will be a valid IPv4 address. 
#  n will be an integer in the range [1, 1000]. 
#  
#  Related Topics Bit Manipulation


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        start = self.ip_to_int(ip)
        ans = []
        while n:
            mask = min((start & -start).bit_length(), n.bit_length())
            ans.append(self.int_to_ip(start)+'/'+str(33-mask))
            start += 1<<(mask-1)
            n -= 1<< (mask-1)
        return ans

    def ip_to_int(self, ip):
        ans = 0
        for x in ip.split('.'):
            ans = ans* 256 + int(x)
        return ans

    def int_to_ip(self, num):
        ans = []
        for _ in range(4):
            ans.append(num%256)
            num = num//256
        ans.reverse()
        return '.'.join([str(x) for x in ans])

        
# leetcode submit region end(Prohibit modification and deletion)
