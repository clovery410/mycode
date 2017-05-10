class Twitter(object):
    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId):
        tweets = self.tweets
        res = []
        res.extend(tweets[userId][-10:])
        for followeeId in self.followers[userId]:
            res.extend(tweets[followeeId][-10:])
            
        res.sort(reverse = True)
        return [x[1] for x in res[:10]]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followers[followerId].discard(followeeId)

#solution2, use heap to improve time complexcity
from heapq import *
class Twitter2(object):
    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId):
        tweets = self.tweets
        candidates = []
        candidates.extend(tweets[userId][-10:])
        for followeeId in self.followers[userId]:
            candidates.extend(tweets[followeeId][-10:])
        heapify(candidates)
        return [x[1] for x in nlargest(10, candidates)]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followers[followerId].discard(followeeId)

# continue to improve solution2, only do 10 times heappop at most
class Tiwtter3(object):
    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append([-self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId):
        tweets = self.tweets
        candidates, news = [], []
        for followeeId in (self.followers[userId] | {userId}):
            if tweets[followeeId]:
                timestamp, tweet = tweets[followeeId][-1]
                index = len(tweets[followeeId]) - 1
                heappush(candidates, (timestamp, tweet, followeeId, index))
        for i in range(10):
            if candidates:
                timestamp, tweet, followeeId, index = heappop(candidates)
                news.append(tweet)
                if index:
                    new_timestamp, new_tweet = tweets[followeeId][index-1]
                    heappush(candidates, (new_timestamp, new_tweet, followeeId, index-1))
        return news

    def follow(self, followerId, followeeId):
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followers[followerId].discard(followeeId)



        
