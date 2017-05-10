import collections
def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    recommendation = []
    follows = getFollowingRelationship(followGraph_edges)
    liked_tweets = getLikedTweets(likeGraph_edges)
    tweets_count = collections.defaultdict(int)
    following_list = follows[targetUser]
    for person in following_list:
        for tweet in liked_tweets[person]:
            tweets_count[tweet] += 1
    for tweet, count in tweets_count.items():
        if count >= minLikeThreshold:
            recommendation.append(tweet)
    return sorted(recommendation)

def getFollowingRelationship(followGraph_edges):
    follows = collections.defaultdict(set)
    for follower, followee in followGraph_edges:
        follows[follower].add(followee)
    return follows

def getLikedTweets(likeGraph_edges):
    liked_tweets = collections.defaultdict(set)
    for person, tweet in likeGraph_edges:
        liked_tweets[person].add(tweet)
    return liked_tweets

    
