from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_to_tweets = defaultdict(list)
        self.user_to_following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_following[userId].add(userId)
        self.user_to_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        for followeeId in self.user_to_following[userId]:
            if followeeId in self.user_to_tweets:
                index = len(self.user_to_tweets[followeeId]) - 1
                count, tweetId = self.user_to_tweets[followeeId][index]
                minHeap.append((count, tweetId, followeeId, index - 1))

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.user_to_tweets[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_to_following[followerId]:
            self.user_to_following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)