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
        heapq.heapify(minHeap) #unique nums now a heap

        while minHeap:
            minCard = heapq.heappop(minHeap) #keep popping min from heap (this happens after each group of groupSize created)
            count = freqs[minCard] #store the frequency of this min
            if count > 0: #if this min exists
                for i in range(groupSize): #try to create a group of groupSize
                    if freqs.get(minCard + i, 0) < count: #if we can't find the next num, return False
                    #we check vs. count here so we check every group starting with minCard at once,
                    # ex: if there are 2 1's, we will need two 2's, as there will be multiple groups starting with 1
                        return False 
                    freqs[minCard + i] -= count #if we have found the next num, decrement freq by 1

        return True

        #track the frequency of cards with hashmap
        #loop through from minimum and keep incrementing by 1:
            # if we cannot find value in hashmap, then we return false
            # if we can find value -> decrement it's frequency by 1, append to subset, move to next
            # if subset.length == groupSize, go back to minimum remaining number -> store all the numbers in a minHeap
            # if we make it to end, return True

