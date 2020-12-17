#Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. 
#
# Machine 1 (sender) has the function: 
#
# 
#string encode(vector<string> strs) {
#  // ... your code
#  return encoded_string;
#} 
#Machine 2 (receiver) has the function:
#
# 
#vector<string> decode(string s) {
#  //... your code
#  return strs;
#}
# 
#
# So Machine 1 does: 
#
# 
#string encoded_string = encode(strs);
# 
#
# and Machine 2 does: 
#
# 
#vector<string> strs2 = decode(encoded_string);
# 
#
# strs2 in Machine 2 should be the same as strs in Machine 1. 
#
# Implement the encode and decode methods. 
#
# 
#
# Note: 
#
# 
# The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters. 
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless. 
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm. 
# 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)

    def len_to_str(self, x):
        l = len(x)
        bytes =  [chr(l>>(i*8) & 0xff) for i in range(4)]
        bytes.reverse()
        return ''.join(bytes)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i = 0
        n = len(s)
        output = []
        while i<n:
            l = self.str_to_len(s[i:i+4])
            i += 4
            t = s[i:i+l].decode('utf-8')
            i += l
            output.append(t)
        return output

    def str_to_len(self, x):
        ans = 0
        for ch in x:
            ans = ans*256+ord(ch)
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
#leetcode submit region end(Prohibit modification and deletion)
