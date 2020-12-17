# Given a url startUrl and an interface HtmlParser, implement a web crawler to c
# rawl all links that are under the same hostname as startUrl. 
# 
#  Return all urls obtained by your web crawler in any order. 
# 
#  Your crawler should: 
# 
#  
#  Start from the page: startUrl 
#  Call HtmlParser.getUrls(url) to get all urls from a webpage of given url. 
#  Do not crawl the same link twice. 
#  Explore only the links that are under the same hostname as startUrl. 
#  
# 
#  
# 
#  As shown in the example url above, the hostname is example.org. For simplicit
# y sake, you may assume all urls use http protocol without any port specified. Fo
# r example, the urls http://leetcode.com/problems and http://leetcode.com/contest
#  are under the same hostname, while urls http://example.org/test and http://exam
# ple.com/abc are not under the same hostname. 
# 
#  The HtmlParser interface is defined as such: 
# 
#  
# interface HtmlParser {
#   // Return a list of all urls from a webpage of given url.
#   public List<String> getUrls(String url);
# } 
# 
#  Below are two examples explaining the functionality of the problem, for custo
# m testing purposes you'll have three variables urls, edges and startUrl. Notice 
# that you will only have access to startUrl in your code, while urls and edges ar
# e not directly accessible to you in code. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input:
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com",
#   "http://news.yahoo.com/us"
# ]
# edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
# startUrl = "http://news.yahoo.com/news/topics/"
# Output: [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.yahoo.com/us"
# ]
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: 
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com"
# ]
# edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
# startUrl = "http://news.google.com"
# Output: ["http://news.google.com"]
# Explanation: The startUrl links to all other pages that do not share the same 
# hostname. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= urls.length <= 1000 
#  1 <= urls[i].length <= 300 
#  startUrl is one of the urls. 
#  Hostname label must be from 1 to 63 characters long, including the dots, may 
# contain only the ASCII letters from 'a' to 'z', digits from '0' to '9' and the h
# yphen-minus character ('-'). 
#  The hostname may not start or end with the hyphen-minus character ('-'). 
#  See: https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames 
#  You may assume there're no duplicates in url library. 
#  
#  Related Topics Depth-first Search Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        ans = []
        queue = collections.deque()

        def get_hostname(url):
            return url.split('/')[2]

        hostname = get_hostname(startUrl)

        queue.append(startUrl)
        visited = set()
        visited.add(startUrl)
        while queue:
            url = queue.popleft()
            ans.append(url)
            for url1 in htmlParser.getUrls(url):
                if url1 in visited: continue
                if get_hostname(url1) != hostname: continue
                queue.append(url1)
                visited.add(url1)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
