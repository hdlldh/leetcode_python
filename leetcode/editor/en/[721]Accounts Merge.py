# Given a list accounts, each element accounts[i] is a list of strings, where th
# e first element accounts[i][0] is a name, and the rest of the elements are email
# s representing emails of the account. 
# 
#  Now, we would like to merge these accounts. Two accounts definitely belong to
#  the same person if there is some email that is common to both accounts. Note th
# at even if two accounts have the same name, they may belong to different people 
# as people could have the same name. A person can have any number of accounts ini
# tially, but all of their accounts definitely have the same name. 
# 
#  After merging the accounts, return the accounts in the following format: the 
# first element of each account is the name, and the rest of the elements are emai
# ls in sorted order. The accounts themselves can be returned in any order. 
# 
#  Example 1: 
#  
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnn
# ybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Ma
# ry", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.
# com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email "
# johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses
#  are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'ma
# ry@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] wo
# uld still be accepted.
#  
#  
# 
#  Note:
#  The length of accounts will be in the range [1, 1000]. 
#  The length of accounts[i] will be in the range [1, 10]. 
#  The length of accounts[i][j] will be in the range [1, 30]. 
#  Related Topics Depth-first Search Union Find


# leetcode submit region begin(Prohibit modification and deletion)
class DSU(object):
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, i):
        while self.p[i] != i:
            i = self.p[i]
        return i

    def union(self, i, j):
        self.p[self.find(i)] = self.find(j)


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        dsu = DSU(n)
        em_to_name = {}
        em_to_id = {}
        for i, acc in enumerate(accounts):
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                dsu.union(em_to_id[email], i)

        id_to_em = collections.defaultdict(list)
        for email in em_to_name:
            id_to_em[dsu.find(em_to_id[email])].append(email)

        ans = []
        for i, em in id_to_em.items():
            ans.append([accounts[i][0]] + sorted(em))
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
