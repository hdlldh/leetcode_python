#Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods: 
#
# 
# 
# postTweet(userId, tweetId): Compose a new tweet. 
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. 
# follow(followerId, followeeId): Follower follows a followee. 
# unfollow(followerId, followeeId): Follower unfollows a followee. 
# 
# 
#
# Example:
# 
#Twitter twitter = new Twitter();
#
#// User 1 posts a new tweet (id = 5).
#twitter.postTweet(1, 5);
#
#// User 1's news feed should return a list with 1 tweet id -> [5].
#twitter.getNewsFeed(1);
#
#// User 1 follows user 2.
#twitter.follow(1, 2);
#
#// User 2 posts a new tweet (id = 6).
#twitter.postTweet(2, 6);
#
#// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
#// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
#twitter.getNewsFeed(1);
#
#// User 1 unfollows user 2.
#twitter.unfollow(1, 2);
#
#// User 1's news feed should return a list with 1 tweet id -> [5],
#// since user 1 is no longer following user 2.
#twitter.getNewsFeed(1);
# 
# Related Topics Hash Table Heap Design



#leetcode submit region begin(Prohibit modification and deletion)
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeId = 0
        self.followee = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append((self.timeId, tweetId))
        self.timeId += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        news = []
        for tweet in self.tweets[userId]:
            heapq.heappush(news, tweet)
            if len(news)>10: heapq.heappop(news)
        for follower in self.followee[userId]:
            for tweet in self.tweets[follower]:
                heapq.heappush(news, tweet)
                if len(news) > 10: heapq.heappop(news)
        ans = []
        while news:
            timeId, tweetId = heapq.heappop(news)
            ans.append(tweetId)
        ans.reverse()
        return ans

        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId!=followerId: self.followee[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followee[followerId]: self.followee[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
#leetcode submit region end(Prohibit modification and deletion)
