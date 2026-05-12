# WTF IS WRONG WITH THIS

# postTweet:   O(1) time, O(1) space
# getNewsFeed: O(f + 10 log f) time, O(f) space
# follow:      O(1) time, O(1) space
# unfollow:    O(1) time, O(1) space
class Twitter:

    def __init__(self):
        # Store tweets by user and track follow relationships.
        # count acts like a timestamp; smaller values mean newer tweets.
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add a new tweet for the user with its timestamp.
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Include the user's own tweets in their feed.
        self.followMap[userId].add(userId)

        # Add the most recent tweet from each followed user to the heap.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        # Repeatedly pull the newest tweet, then add the next older tweet
        # from the same user, until the feed has at most 10 tweets.
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(
                    minHeap,
                    [count, tweetId, followeeId, index - 1]
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Record that followerId follows followeeId.
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the follow relationship, but keep users following themselves.
        if followerId != followeeId:
            self.followMap[followerId].discard(followeeId)