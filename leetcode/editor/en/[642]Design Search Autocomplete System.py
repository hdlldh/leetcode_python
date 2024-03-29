# Design a search autocomplete system for a search engine. Users may input a sen
# tence (at least one word and end with a special character '#'). For each charact
# er they type except '#', you need to return the top 3 historical hot sentences t
# hat have prefix the same as the part of sentence already typed. Here are the spe
# cific rules: 
# 
#  
#  The hot degree for a sentence is defined as the number of times a user typed 
# the exactly same sentence before. 
#  The returned top 3 hot sentences should be sorted by hot degree (The first is
#  the hottest one). If several sentences have the same degree of hot, you need to
#  use ASCII-code order (smaller one appears first). 
#  If less than 3 hot sentences exist, then just return as many as you can. 
#  When the input is a special character, it means the sentence ends, and in thi
# s case, you need to return an empty list. 
#  
# 
#  Your job is to implement the following functions: 
# 
#  The constructor function: 
# 
#  AutocompleteSystem(String[] sentences, int[] times): This is the constructor.
#  The input is historical data. Sentences is a string array consists of previousl
# y typed sentences. Times is the corresponding times a sentence has been typed. Y
# our system should record these historical data. 
# 
#  Now, the user wants to input a new sentence. The following function will prov
# ide the next character the user types: 
# 
#  List<String> input(char c): The input c is the next character typed by the us
# er. The character will only be lower-case letters ('a' to 'z'), blank space (' '
# ) or a special character ('#'). Also, the previously typed sentence should be re
# corded in your system. The output will be the top 3 historical hot sentences tha
# t have prefix the same as the part of sentence already typed. 
#  
# 
#  Example: 
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetc
# ode"], [5,3,2,2]) 
# The system have already tracked down the following sentences and their corresp
# onding times: 
# "i love you" : 5 times 
# "island" : 3 times 
# "ironman" : 2 times 
# "i love leetcode" : 2 times 
# Now, the user begins another search: 
#  
# Operation: input('i') 
# Output: ["i love you", "island","i love leetcode"] 
# Explanation: 
# There are four sentences that have prefix "i". Among them, "ironman" and "i lo
# ve leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII
#  code 114, "i love leetcode" should be in front of "ironman". Also we only need 
# to output top 3 hot sentences, so "ironman" will be ignored. 
#  
# Operation: input(' ') 
# Output: ["i love you","i love leetcode"] 
# Explanation: 
# There are only two sentences that have prefix "i ". 
#  
# Operation: input('a') 
# Output: [] 
# Explanation: 
# There are no sentences that have prefix "i a". 
#  
# Operation: input('#') 
# Output: [] 
# Explanation: 
# The user finished the input, the sentence "i a" should be saved as a historica
# l sentence in system. And the following input will be counted as a new search. 
#  
# 
#  Note: 
# 
#  
#  The input sentence will always start with a letter and end with '#', and only
#  one blank space will exist between two words. 
#  The number of complete sentences that to be searched won't exceed 100. The le
# ngth of each sentence including those in the historical data won't exceed 100. 
#  Please use double-quote instead of single-quote when you write test cases eve
# n for a character input. 
#  Please remember to RESET your class variables declared in class AutocompleteS
# ystem, as static/class variables are persisted across multiple test cases. Pleas
# e see here for more details. 
#  
# 
#  
#  Related Topics Design Trie


# leetcode submit region begin(Prohibit modification and deletion)
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = {}
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i])
        self.word = ''

    def add(self, word, freq):
        p = self.root
        for ch in word:
            p = p.setdefault(ch, {})
        p['#'] = freq

    def search(self, word):
        p = self.root
        for ch in word:
            if ch not in p:
                return None
            p = p[ch]
        return p

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            p = self.search(self.word)
            # print(self.root)
            if p and '#' in p:
                p['#'] += 1
            else:
                self.add(self.word, 1)
            self.word = ''
            return []

        heap = []
        self.word += c
        p = self.search(self.word)
        if not p: return []

        def dfs(p, out, heap):
            for key, val in p.items():
                if key == '#':
                    heapq.heappush(heap, (-val, out))
                else:
                    dfs(val, out + key, heap)

        dfs(p, self.word, heap)
        ans = []
        cnt = 3
        while heap and cnt > 0:
            cnt -= 1
            _, out = heapq.heappop(heap)
            ans.append(out)

        return ans
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# leetcode submit region end(Prohibit modification and deletion)
