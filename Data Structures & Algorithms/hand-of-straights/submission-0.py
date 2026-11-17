import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        #create our frequency map:
        freqs = {}
        for num in hand:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1

        minHeap = list(freqs.keys())
        heapq.heapify(minHeap)

        while minHeap:
            minCard = heapq.heappop(minHeap)
            count = freqs[minCard]
            if count > 0:
                for i in range(groupSize):
                    if freqs.get(minCard + i, 0) < count:
                        return False
                    freqs[minCard + i] -= count

        return True

        #track the frequency of cards with hashmap
        #loop through from minimum and keep incrementing by 1:
            # if we cannot find value in hashmap, then we return false
            # if we can find value -> decrement it's frequency by 1, append to subset, move to next
            # if subset.length == groupSize, go back to minimum remaining number -> store all the numbers in a minHeap
            # if we make it to end, return True

